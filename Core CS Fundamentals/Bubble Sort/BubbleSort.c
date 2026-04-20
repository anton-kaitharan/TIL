// Online C compiler to run C program online
#include <stdio.h>
#include <stdbool.h>

void swap(int* xp, int* yp){
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void bubbleSort(int arr[], int n){
    int i, j;
    for(i=0;i<n-1;i++){
        bool swapped = false;
        for(j=0;j<(n-i-1);j++){
            if (arr[j]>arr[j+1]){
                swapped = true;
                swap(&arr[j], &arr[j+1]);
            }
        }
        if(swapped == false){
            break;
        }
    }
}

void printArray(int arr[], int size){
    int i;
    printf(" Bubble Sorted: ");
    for(i=0;i<size;i++){
        printf("%d ", arr[i]);
    }
    
}

int main() {
    int arr[] = { 64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    bubbleSort(arr, n);
    printArray(arr,n);
    
}