bool isPalindrome(int x) {
    
    int rem=0,temp;
    long int sum=0;
    temp=x;

    while(x>0)
    {
        rem=x%10;
        sum=sum*10+rem;
        x/=10;
    }
    if(temp==sum)
    {
        return true;
    }
    else 
    {
        return  false;
    }
}

