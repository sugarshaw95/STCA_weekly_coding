class Solution {
public:
    int getSum(int a, int b) {
        //int x=-3<<1;
        //unsigned int x=-3;
        //cout<<x;
        while (b!=0)
        {
            //cout<<a<<endl;
            //cout<<b<<endl;
            int wu=a^b;//无进位加法结果
            int jin=(unsigned int)(a&b)<<1;  //进位 
            a=wu;
            b=jin;
            //循环直到无进位
        }
        return a;


    }
};