/*********************************************function library**********************************************/
#include "fun.h"

extern "C" {
    char* encryption(char* msg, int key) {
        int len = 0;
        for (char* p = msg; *p != '\0'; ++p) {
            char c = *p;
            if (c >= 'a' && c <= 'z') {
                ++len;
            }
        }
        char* msg_encrypted = new char[len + 1];
        char* p = msg_encrypted;
        for (char* q = msg; *q != '\0'; ++q) {
            char c = *q;
            if (c >= 'a' && c <= 'z') {
                *p++ = c + key;
            }
        }
        *p = '\0';
        return msg_encrypted;
    }

    char* decryption(char* msg, int key) {
        int len = 0;
        for (char* p = msg; *p != '\0'; ++p) {
            char c = *p;
            if (c >= 'a' && c <= 'z') {
                ++len;
            }
        }
        char* msg_decrypted = new char[len + 1];
        char* p = msg_decrypted;
        for (char* q = msg; *q != '\0'; ++q) {
            char c = *q;
            if (c >= 'a' && c <= 'z') {
                *p++ = c - key;
            }
        }
        *p = '\0';
        return msg_decrypted;
    }
}
