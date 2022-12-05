#include <fstream>
#include <iostream>
#include <numeric>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

template <typename T>
class fixed_priority_queue : private std::priority_queue<T> {
   public:
    fixed_priority_queue(unsigned int size) : fixed_size(size) {}

    void push(const T& x) {
        if (this->size() == fixed_size) {
            auto beg = this->c.begin();
            auto end = this->c.end();
            auto min = std::min_element(beg, end);

            if (x > *min) {
                *min = x;
                std::make_heap(beg, end);
            }
        } else {
            this->priority_queue::push(x);
        }
    }

    std::vector<int> get_all() {
        return this->c;
    }

   private:
    const unsigned int fixed_size;
};

int main() {
    std::ifstream myfile("input");
    std::string line;

    int current = 0;
    int line_calories = 0;

    fixed_priority_queue pq = fixed_priority_queue<int>(3);

    while (std::getline(myfile, line)) {
        std::istringstream iss(line);

        if (!(iss >> line_calories)) {
            pq.push(current);
            current = 0;
            continue;
        }

        current += line_calories;
    }

    std::vector<int> top_calories = pq.get_all();

    std::cout << "Max calories = "
              << accumulate(top_calories.begin(), top_calories.end(), 0)
              << std::endl;
    return 0;
}
