#include "widget2.h"
#include "ui_widget2.h"
#include <unistd.h>
#include <QTimer>

widget2::widget2(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::widget2)
{
    ui->setupUi(this);
    this->setFixedSize(this->width(), this->height());
    this->move(1200, 400);

    int pid = getpid();
    ui->lcdNumber_6->display(pid);

    sum = 0;
    num = 1;
    ui->lcdNumber_8->display(sum);

    QTimer *timer = new QTimer(this);
    connect(timer, SIGNAL(timeout()), this, SLOT(Update()));
    timer->start(1000);
}

void widget2::Update(){
    if(num <= 1000)
        sum += num++;
    ui->lcdNumber_8->display(sum);
    ui->lcdNumber_7->display(num-1);
}
widget2::~widget2()
{
    delete ui;
}
