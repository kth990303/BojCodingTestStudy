#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cctype>

using namespace std;


//signal: aborted (core dumped) 에러로 채점 불가능

bool sorttt(vector<string> a, vector<string> b) {
    int aa = stoi(a[0]);
    int bb = stoi(b[0]);
    int aaa = tolower(aa);
    int bbb = tolower(bb);
    if (aaa < bbb) {
        return true;
    } else if (aaa > bbb) {
        return false;
    } else {
        if (stoi(a[1]) <= stoi(b[1])) {
            return true;
        } else {
            return false;
        }
    }
}


vector<string> solution(vector<string> files) {
    vector<string> answer;
    vector<vector<string>> cache; //temp1
    
    //head, number, tail divide and conquer
    for (int z = 0; z < files.size(); z++) {
        vector<string> cache_space;//temp2 
        int i = 0;
        
        //head
        string head = "";
        while (i < files[z].size() && !isdigit(files[z][i])) {
            head.push_back(files[z][i]);
            i++;
        }      
        cache_space.push_back(head);

        //number
        string number = "";
        while (i < files[z].size() && isdigit(files[z][i])) {
            number.push_back(files[z][i]);
            i++;
        }
        
        //tail
        cache_space.push_back(number);        
        string tail = "";
        while (i < files[z].size()) {
            tail.push_back(files[z][i]);
            i++;
        }
        cache_space.push_back(tail);

        //push back to temp1
        cache.push_back(cache_space);
    }
    
    //sorting
    for (int z = 0; z < cache.size() - 1; z++) {
        for (int w = z + 1; w < cache.size(); w++) {
            if (!sorttt(cache[z], cache[w])) {
                vector<string> temp = cache[z];
                cache[z] = cache[w];
                cache[w] = temp;
            }
        }
    }
    
    //making answer and return
    for (int z = 0; z < cache.size(); z++) {
        string comb = "";
        for (int i = 0; i < 3; i++) {
            comb += cache[z][i];
        }
        answer.push_back(comb);
    }
    return answer;
}