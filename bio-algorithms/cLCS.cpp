#include <iostream>
#include <fstream>
#include <string>
#include <cassert>
#include <vector>
#include <queue>

using namespace std;


char* LCS(const char* X, const char* Y, const int m, const int n){
	/*if (m == 0 || n == 0)
	 return 0;
	 if (X[m-1] == Y[n-1])
	 return 1 + LCS(X, Y, m-1, n-1);
	 else
	 return max(LCS(X, Y, m, n-1), LCS(X, Y, m-1, n));*/
	
	int C[m+1][n+1];
	int i, j, k;
	
	for (i=0; i<=m; i++)
	{
		for (j=0; j<=n; j++)
		{
			if (i == 0 || j == 0)
				C[i][j] = 0;
			else if (X[i-1] == Y[j-1])
				C[i][j] = C[i-1][j-1] + 1;
			else
				C[i][j] = max(C[i-1][j], C[i][j-1]);
		}
	}
    
	/* L[m][n] contains length of LCS for X[0..n-1] and Y[0..m-1] */
	int length = C[m][n];
	
	char Sequence[length];
	i = m-1;
	j = n-1;
	k = 0;
	while( i >= 0 && j >= 0){
		if(X[i] == Y[j]){
			Sequence[k++] = X[i];
			i--; j--;
		}
		else if (C[i-1,j] > C[i,j-1])
			i--;
		else
			j--;
	}
	return Sequence;
}

int main(int argc, char *argv[]) {
	char* x = "BDCABA";
	char* y = "ABCBDAB";
	
	cout<<LCS(x,y,6,7);
	cout<<endl;
	
	return 0;
}
