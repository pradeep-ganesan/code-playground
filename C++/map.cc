#include <iostream>
#include <map>

bool findItem(std::map<char,int>, char) {
    return true;
}

int main()
{
    std::map<char,int> mymap;
    mymap.insert(std::pair<char,int>('a',1));
    mymap.insert(std::pair<char,int>('b',1));
    mymap.insert(std::pair<char,int>('c',1));

    for(int j='d'; j<='l'; j++) {
        mymap[j] += 1;
    }
    mymap['c'] += 1;

    int maxval = 0;
    char maxkey = 0;
    for(std::map<char,int>::iterator it=mymap.begin(); it!=mymap.end(); it++) {
        if (it->second > maxval) {
            maxkey = it->first;
            maxval = it->second;
        }
        std::cout << it->first << " " << it->second << "\n";
    }
    std::cout << "Maxkey: " << maxkey << " maxval: " << maxval << "\n";

    return 0;
}