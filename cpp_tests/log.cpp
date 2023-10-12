#include <iostream>


class Log{

public: 
    const int logLevelError=0;
    const int logLevelWarning=1;
    const int logLevelInfo=2;

private:
    int m_logLevel=logLevelInfo; //m_ tells me that it's a private class-level var. Not a local variable. by default, set to info.
public:
    void setLevel(int level){
        m_logLevel = level;
    }

    void warning(const char* message){
        if(m_logLevel>=logLevelWarning){
            std::cout<<"Warning: "<<message<<std::endl;
        }
    }
    void error(const char* message){
        if(m_logLevel>=logLevelError){
            std::cout<<"Error: "<<message<<std::endl;
        }
    }
    void info(const char* message){
        if(m_logLevel>=logLevelInfo){
            std::cout<<"Info: "<<message<<std::endl;
        }
    }
};

int input();
int a =10;
int main(){
    input();
    std::cout<<a<<std::endl;
    Log log;
    log.setLevel(log.logLevelInfo); //filter level. info, warnings, errors. 
    log.warning("oopsie!");
    log.error("ooo you done messed up");
    
}