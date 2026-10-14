//Roll No.:2610110341
// Name: Gokul Sakar Reddy Malapati

#include <stdio.h>
#include <stdlib.h>

int main(){
    int arr[100],i,n,maxfreq;
    int freq[11]={0};
   for(i=0;i<100;i++){
       arr[i] = 10 + (rand()%11);
   }
   printf("The Original Array: ");
   for(i=0;i<100;i++){
       printf("%d ",arr[i]);
   }
   printf("\n\n");
   for(i=0;i<100;i++){
       if(arr[i]==10)
           freq[0] ++;
       else if(arr[i]==11)
           freq[1]++;
       else if(arr[i]==12)
           freq[2]++;
       else if(arr[i]==13)
           freq[3]++;
       else if(arr[i]==14)
           freq[4]++;
       else if(arr[i]==15)
           freq[5]++;
       else if(arr[i]==16)
           freq[6]++;
       else if(arr[i]==17)
           freq[7]++;
       else if(arr[i]==18)
           freq[8]++;
       else if(arr[i]==19)
           freq[9]++;
       else
           freq[10]++;
   }
   for(n=10;n<21;n++){
       if(freq[n-10]>0)
           printf("%d, Frequency:%d ||",n,freq[n-10]);
   }
   maxfreq = freq[0];
   for(n=0;n<11;n++){
       if(freq[n]>maxfreq)
           maxfreq = freq[n];
   }
   for(n=0;n<11;n++){
       if(freq[n]==maxfreq){
           printf("The Number with Maximum Frequency:%d , Frequency:%d\n",n+10,maxfreq);
       }
   }

}
