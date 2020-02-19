#include "widget.h"
#include "widget1.h"
#include "widget2.h"
#include <QApplication>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    int pid;
    if((pid  = fork()) == 0){
        QApplication a(argc, argv);//Create an application
        widget1 w;//Create a widget
        w.move(100,200);
        w.setWindowTitle("Counter");
        w.show();
        a.exec();
        exit(0);
    }
    if((pid  = fork()) == 0){
        QApplication a(argc, argv);
        widget2 w;
        w.move(300,400);
        w.setWindowTitle("Accumulator");
        w.show();
        a.exec();
        exit(0);
    }
    QApplication a(argc, argv);
    Widget w;
    w.move(500,600);
    w.setWindowTitle("Clock");
    w.show();
    return a.exec();
}
