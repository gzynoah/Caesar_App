#ifndef FUN_H
#define FUN_H



extern "C" {
    __declspec(dllexport) char* encryption(char* msg, int key);
    __declspec(dllexport) char* decryption(char* msg, int key);
}

#endif
