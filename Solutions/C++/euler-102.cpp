#include<fstream>
#include<iostream>
#include<string>
#include<vector>

using namespace std;

struct Point {
    int x;
    int y;
    Point(int x_, int y_) {
        x = x_;
        y = y_;
    }
};

vector<Point> parse_string(string s)
{
    vector<int> numbers;
    string tmp;
    for(int i = 0; i < s.length(); i++) {
        if(s[i] != ',') {
            tmp.push_back(s[i]);
        } else {
            if(tmp.length() > 0) {
                numbers.push_back(stoi(tmp));
            }
            tmp = "";
        }
    }
    
    if(tmp.length() > 0) {
        numbers.push_back(stoi(tmp));
    }

    vector<Point> points;
    for(int i = 0; i < numbers.size(); i+=2) {
        Point p(numbers[i],numbers[i+1]);
        points.push_back(p);
    }

    return points;
}

int triangle_area(vector<Point> points) {
    return (points[0].x - points[2].x) * (points[1].y - points[2].y) - (points[1].x - points[2].x) * (points[0].y - points[2].y);
}

bool inside_triangle(vector<Point> points)
{
    Point origin(0,0);
    
    int area_1 = triangle_area({origin,points[0],points[1]});
    int area_2 = triangle_area({origin,points[1],points[2]});
    int area_3 = triangle_area({origin,points[2],points[0]});

    bool has_neg_area = (area_1 < 0) || (area_2 < 0) || (area_3 < 0);
    bool has_pos_area = (area_1 > 0) || (area_2 > 0) || (area_3 > 0);

    return !(has_neg_area && has_pos_area);
}


int find_triangles() {
    fstream in("euler-102-data.txt");
    string line;
    int count = 0;
    while(!in.eof()) {
        in >> line;
        
        vector<Point> points = parse_string(line);

        if(inside_triangle(points)) {
            ++count;
        }
    }

    in.close();
    return count;
}

int main() 
{
    
    int triangles_count = find_triangles();
    cout << triangles_count << "\n";
    return 0;
}