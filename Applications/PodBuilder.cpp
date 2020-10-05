#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <Windows.h>

void newLineReturn(HWND hwnd)
{
    INPUT input;
    WORD vkey = VK_RETURN; // see link below
    input.type = INPUT_KEYBOARD;
    input.ki.wScan = MapVirtualKey(vkey, MAPVK_VK_TO_VSC);
    input.ki.time = 0;
    input.ki.dwExtraInfo = 0;
    input.ki.wVk = vkey;
    input.ki.dwFlags = 0; // there is no KEYEVENTF_KEYDOWN
    SendInput(1, &input, sizeof(INPUT));

    input.ki.dwFlags = KEYEVENTF_KEYUP;
    SetForegroundWindow(hwnd);
    SendInput(1, &input, sizeof(INPUT));
}

HWND getBrowser(){
    std::vector<LPCSTR> iterateBrowsers= {"Chrome_WidgetWin_1", "Chrome", "Mozilla Firefox", "MozillaWindowClass"};
    for (LPCSTR& browser : iterateBrowsers){
        HWND hwnd = FindWindow(browser, nullptr);
        if (hwnd) {
            return hwnd;
        }
        else {
            std::cout << browser << " Not Found!\n";
        }
    }
}

void keyBoardOutput(const std::string& msg, HWND hwnd)
{
    std::vector<INPUT> vec;
    for(char ch : msg)
    {
        INPUT input = { 0 };
        input.type = INPUT_KEYBOARD;
        input.ki.dwFlags = KEYEVENTF_UNICODE;
        input.ki.wScan = ch;
        vec.push_back(input);

        input.ki.dwFlags |= KEYEVENTF_KEYUP;
        vec.push_back(input);
    }
    SetForegroundWindow(hwnd);
    SendInput(vec.size(), vec.data(), sizeof(INPUT));
}

std::vector<std::string> stripArrayEmpty(std::vector<std::string> main_array){
    for (int i = 0; i < main_array.size();) {
        if (main_array[i].empty()) {
            main_array.erase(main_array.begin() + i);
        } else ++i;
    }
    return main_array;
}

std::vector<std::string> returnBins(std::string recipe) {
    std::string delimiter = ">";
    std::string t_string;
    std::vector<std::string> main_array(256);
    int count = 0;
    size_t pos;

    while ((pos = recipe.find(delimiter)) != std::string::npos) {
        t_string = recipe.substr(0, pos);
        std::replace(t_string.begin(), t_string.end(), '*', '-'); // replace all 'x' to 'y'
        recipe.erase(0, pos + delimiter.length());
        main_array[count] = t_string;
        count += 1;
    }
    std::replace(recipe.begin(), recipe.end(), '*', '-'); // replace all 'x' to 'y'
    recipe.erase(recipe.end()-1, recipe.end());
    main_array[count] = recipe;
    main_array = stripArrayEmpty(main_array);
    main_array.erase(main_array.begin());
    return main_array;
}

std::vector<std::string> returnFace(const char& faceChar, const std::vector<std::string>& binArray) {
    std::vector<std::string> faceArray(256);
    int count = 0;

    for (const auto & bin : binArray)
    {
        if (bin.at(0) == faceChar) {
            faceArray[count] = bin;
            count += 1;
        }
    }
    return stripArrayEmpty(faceArray);
}

std::vector<std::string> getArray(std::vector<std::string>& faceArray){
    std::vector<std::string> invertedArray(256);
    std::vector<std::basic_string<char>> letters = {"M", "L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A"};
    std::basic_string<char> tempLetter = "X";
    int count = 0;
    std::vector<std::string> staticArray = faceArray;

    for (const std::basic_string<char>& letter : letters ){
        for (std::string& bin : staticArray){
            tempLetter = bin.at(2);
            if (letter == tempLetter){
                bin.erase(bin.begin(), bin.begin() + 3);
                invertedArray[count] = bin;
                count += 1;
            }
        }
    }
    return stripArrayEmpty(invertedArray);
}

std::vector<std::vector<std::string>> dummyReturn(std::string *recipe){
    std::vector<std::string> bins = returnBins(*recipe);
    const char* A = "A";
    const char* B = "B";
    const char* C = "C";
    const char* D = "D";

    std::vector<std::string> AFace = returnFace(*A, bins);
    std::vector<std::string> BFace = returnFace(*B, bins);
    std::vector<std::string> CFace = returnFace(*C, bins);
    std::vector<std::string> DFace = returnFace(*D, bins);

    std::vector<std::string> invertedFaceA = getArray(AFace);
    std::vector<std::string> invertedFaceB = getArray(BFace);
    std::vector<std::string> invertedFaceC = getArray(CFace);
    std::vector<std::string> invertedFaceD = getArray(DFace);
    std::vector<std::vector<std::string>> podRecipe = {invertedFaceA, invertedFaceB, invertedFaceC, invertedFaceD};
    return podRecipe;
}

void stripRecipe(std::string recipe){
    recipe.erase(recipe.begin() + 19, recipe.end());
    std::cout << std::endl << "Recipe | Version:";
    std::string temp_string = recipe.substr(3, 13);
    std::replace(temp_string.begin(), temp_string.end(), '*', '-');
    std::vector<std::string> recipeVersionArray = {temp_string, recipe.substr(17, 2)};
    for (auto& returnThis : recipeVersionArray){
        std::cout << " " << returnThis << " ";
    }
}

int main() {
    int Major = 0;
    int Minor = 1;
    int Patch = 0;

    std::string recipe;
    std::cout << "PodBuilder C++ V." << Major << "." << Minor << "." << Patch << std::endl;
    std::cout << "Scan Recipe: ";
    std::cin >> recipe;
    stripRecipe(recipe);

    HWND hwnd = getBrowser();
    std::vector<std::vector<std::string>>podRecipe = dummyReturn(&recipe);
    char exitString;

    for (const std::vector<std::string>& face : podRecipe){
        for (auto& bin : face){
            keyBoardOutput(bin, hwnd);
            newLineReturn(hwnd);
        }
    }
    std::cin >> exitString;
}
