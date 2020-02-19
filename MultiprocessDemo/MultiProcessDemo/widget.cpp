#include "widget.h"
#include "ui_widget.h"
#include <unistd.h>
#include <QDateTime>
#include <QTimer>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
    this->setFixedSize(this->width(), this->height());//Unable Adjustment of size
    this->move(600, 400);

    int pid = getpid();
    //ui->label_2->setText(QString::number(pid, 10));
    ui->lcdNumber_2->display(pid);

    QDateTime curtime = QDateTime::currentDateTime();
    //ui->label_4->setText(curtime.toString("hh:mm:ss"));

    ui->lcdNumber_3->display(curtime.toString("hh:mm:ss"));
    QTimer *timer = new QTimer(this);
    connect(timer, SIGNAL(timeout()), this, SLOT(Update()));
    timer->start(1000);
}

void Widget::Update(){
    QDateTime curtime = QDateTime::currentDateTime();
    ui->lcdNumber_3->display(curtime.toString("hh:mm:ss"));
   // ui->label_4->setText(curtime.toString("hh:mm:ss"));
}

Widget::~Widget()
{
    delete ui;
}
