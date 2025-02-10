#include <stdio.h>
#include <string.h>

#define KEY 5
#define RANGE 95

int main() {
    char string[100];
    printf("Enter a string: ");
    fgets(string, sizeof(string), stdin);

    size_t len = strlen(string);
    if (string[len - 1] == '\n') {
        string[len - 1] = '\0';
        len--;
    }

    size_t mass_size = (len + 1) / 2;

    short mass[mass_size];
    char *ptr = string;
    short *mass_ptr = mass;

    for (size_t i = 0; i < mass_size; i++, ptr++) {
        char c1 = *ptr;
        char c2 = *(ptr + 1);

        *mass_ptr++ = (short)((c1 << 8) | c2);
        ptr++;
    }

    mass_ptr = mass;
    for (size_t i = 0; i + 1 < mass_size; i += 2) {
        short temp = *(mass_ptr + i);
        *(mass_ptr + i) = *(mass_ptr + i + 1);
        *(mass_ptr + i + 1) = temp;
    }

    char recovered_string[100];
    char *rec_ptr = recovered_string;
    mass_ptr = mass;

    for (size_t i = 0; i < mass_size; i++, mass_ptr++) {
        *rec_ptr++ = (char)((*mass_ptr >> 8) & 0xFF);
        *rec_ptr++ = (char)(*mass_ptr & 0xFF);
    }
    *rec_ptr = '\0';

    rec_ptr = recovered_string;
    size_t recovered_len = strlen(recovered_string);
    for (size_t i = 0; i < recovered_len; i += 2) {
        rec_ptr[i] += 6;
        if (rec_ptr[i] > 126) {
            rec_ptr[i] -= RANGE;
        }

        rec_ptr[i + 1] += 12;
        if (rec_ptr[i + 1] > 126) {
            rec_ptr[i + 1] -= RANGE;
        }
    }

    printf("Recovered string: %s\n", recovered_string);

    return 0;
}
