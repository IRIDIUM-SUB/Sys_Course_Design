/*
 * @Author: I-Hisen
 * @Date: 2020-02-15 20:33:04
 * @LastEditTime: 2020-02-15 20:36:41
 * @LastEditors: Please set LastEditors
 * @Description: 编写一个C程序，用read、write等系统调用实现文件拷贝功能。
 * 命令形式：copy <源文件名> <目标文件名>
 * ref:https://www.cnblogs.com/acerkoo/p/9490308.html
 * ref:https://www.cnblogs.com/smallredness/p/10259237.html
 * ref:https://www.cnblogs.com/smallredness/p/10259232.html
 * ref:https://www.purebasic.com/documentation/filesystem/getfileattributes.html
 * ref:https://blog.csdn.net/cs_zlg/article/details/8271741
 * ref:https://blog.csdn.net/aitcax/article/details/50911445
 */
#include <iostream>
#include <cstring>
#include <fstream>
#include <unistd.h>
#include <sys/stat.h>
using namespace std;
bool fileexist(const char * path);
int filesize(const char *fname);
int main(int argc, char *argv[])
{
    
    if (argc != 4)
    {
        cerr << "Usage: copy <Source> <Dest>" << endl;
        return 0;
    }
    if ((strcmp(argv[1], "copy")))
    {
        cout<<argv[1]<<endl;
        cerr << "Usage: copy <Source> <Dest>" << endl;
        return 0;
    }
    string src = argv[2];
    string dst = argv[3];
    //cout<<src<<"\n"<<dst<<endl;
    if (!fileexist(src.c_str())) //if exitst
    {
        cerr << "Error:No such file" << endl;
        return 0;
    }
    cout << "Comfirm:\n\tSrc:" << src << "\n\tDst:" << dst << "\n\tSize:" << filesize(src.c_str()) << endl;
choosemod:
    cout << "Continue?[Y/n/U(Using read&write)]" << endl;
    string pad;
    cin >> pad;
    if (pad == "Y" || pad == "y" || pad == "")
    {
        //Start standard process:Using stream
        ifstream infile;
        infile.open(src, ios::in | ios::binary); //in bin
        ofstream outfile;
        outfile.open(dst, ios::out | ios::trunc | ios::binary); //recreate and start
        while (!infile.eof())                                   //not an empty file
        {
            char buf[1000] = "";   //initialize buffer
            int len = sizeof(buf); //buffer len
            infile.read(buf, sizeof(buf));
            if (infile.peek() == -1) //handle final block of buffer
            {
                char *p = &buf[len - 1];
                while ((*p) == 0)
                {
                    len--;
                    p--;
                } //to locate eof
            }
            outfile.write(buf, len); //output
        }
        infile.close();  //close
        outfile.flush(); //flush stream
        clog<<"outfile flished"<<endl;
        outfile.close(); //close
        clog << "Process Finished" << endl;
        return 0;
    }
    else if (pad == "U" || pad == "u")
    {
        //Using C style to process
        //But... text or binary?
bd:
        cout << "Binary or Document?\n[B/D]" << endl;
        string bd;
        cin >> bd;
        if (bd == "B" || bd == "b")
        {
            cout << "Comfirm:\n\tBinary Mode" << endl;
            FILE *f1 = fopen(src.c_str(), "rb");
            FILE *f2 = fopen(dst.c_str(), "wb");
            if (!f1 || !f2) //if open successfully
            {
                cerr << "Error: Fail to open file" << endl;
                return 0;
            }
            char buf[1024];
            int len = sizeof(buf);
            while (!feof(f1))
            {
                memset(buf, 0, sizeof(buf)); //initialize buffer
                if (fread(buf, sizeof(buf), 1, f1) != 1)
                {
                    char *p = &buf[len - 1];
                    while ((*p) == 0)
                    {
                        p--;
                        len--;
                    }
                }
                fwrite(buf, len, 1, f2);
            }
            fclose(f1);
            fclose(f2);
            clog << "Binary Mode Succeed" << endl;
            return 0;
        }
        else if (bd == "D" || bd == "d")
        {
            cout << "Comfirm:\n\tDocument Mode" << endl;
            FILE *f1 = fopen(src.c_str(), "r");
            FILE *f2 = fopen(dst.c_str(), "w");
            if (!f1 || !f2)
            {
                cerr << "Error: Fail to open file" << endl;
                return -1;
            }
            char buf[50];
            while (fgets(buf, sizeof(buf), f1) != NULL)
            {
                cout<<buf<<endl;
                fputs(buf, f2);
            }
            fclose(f1);
            fclose(f2);
            clog << "Docunent Mode Succeed" << endl;
        }
        else
        {
            goto bd;
        }
    }
    else if(pad=="n"||pad=="N")
    {
        clog<<"Quit without Operation"<<endl;
        return 0;
    }
    else
    {
        goto choosemod;
    }
}
bool fileexist(const char *path)
{
    if (access(path, 0)==0)//0=success -1=failed
    {
        return true;
    }
    else
    {
        return false;
    }
}
int filesize(const char *fname)
{
    struct stat statbuf;
    if (stat(fname, &statbuf) == 0)
        return statbuf.st_size;
    else
        return -1;
}