#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;
// lowerbound https://chanhuiseok.github.io/posts/algo-55/
vector<int> chk[3][2][2][2];

vector<int> solution(vector<string> info, vector<string> query) {
    vector<int> answer;
    int lang, job, pro, food, score;
    string type;
 
    for (int i = 0; i < info.size(); i++) {
        istringstream iss(info[i]);
        getline(iss, type, ' ');
        if(type == "cpp") lang = 0; else if(type == "java") lang = 1; else lang = 2;
        getline(iss, type, ' ');
        if(type == "backend") job = 0; else job = 1;
        getline(iss, type, ' ');
        if(type == "junior") pro = 0; else pro = 1;
        getline(iss, type, ' ');
        if(type == "chicken") food = 0; else food = 1;
        getline(iss, type, ' ');
        score = stoi(type);
        chkVec[lang][job][pro][food].push_back(score);
    }
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 2; j++) {
            for (int k = 0; k < 2; k++) {
                for (int l = 0; l < 2; l++) {
                    sort(chk[i][j][k][l].begin(), chk[i][j][k][l].end());
                }
            }
        }
    }
      
    
  
    return answer;
}
