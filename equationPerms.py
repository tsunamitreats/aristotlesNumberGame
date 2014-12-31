from itertools import *
from datetime import datetime

# It is possible to derive the following equations using Guassian Elimination.  This leaves us with (19!/(19-7)!) combinations instead of a straight brute force of 19! because we only need to solve for the independent variables.

# a = 76 - j - k - n - 2o - p - r - s
# b = j + n + o
# c = -38 + k + o + p + r + s
# d = j + k + o
# e = -38 + k + n + o + p + r
# f = 38 - j - k - n - o - p
# g = 38 - k - o - r
# h = -38 + n + o + p + r + s
# i = 38 - j - k - n - o - r
# l = 38 - p - s
# m = 38 - n - o - p
# q = 38 - r - s

# independent variables are j, k, n, o, p, r, s

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
counter=0
b=0
startTime=datetime.now()

permu = permutations(nums, 7)

for p in islice(permu,0,None,1):
	
	
	#print permutation every 100 million
	counter+=1
	if counter %100000000 == 0:
		print ('Checked 100 million, now at {}'.format(p))
		print ('Time passed: ', datetime.now()-startTime)
	
	j = p[0]
	k = p[1]
	n = p[2]
	o = p[3]
	pp = p[4]
	r = p[5]
	s = p[6]
	
	a = 76 - j - k - n - 2*o - pp - r - s
	b = j + n + o
	c = -38 + k + o + pp + r + s
	d = j + k + o
	e = -38 + k + n + o + pp + r
	f = 38 - j - k - n - o - pp
	g = 38 - k - o - r
	h = -38 + n + o + pp + r + s
	i = 38 - j - k - n - o - r
	l = 38 - pp - s
	m = 38 - n - o - pp
	q = 38 - r - s
	
	
#There are three sets of checks below.  Check if rows add to 38, make sure there are no negative numbers, and make sure we don't have any duplicates.	
	if 	a+b+c==38 and d+e+f+g==38 and h+i+j+k+l==38 and m+n+o+pp==38 and q+r+s==38 and c+g+l==38 and b+f+k+pp==38 and a+e+j+o+s==38 and d+i+n+r==38 and h+m+q==38 and a+d+h==38 and b+e+i+m==38 and c+f+j+n+q==38 and g+k+o+r==38 and l+pp+s==38 and a>0 and b>0 and c>0 and d>0 and e>0 and f>0 and g>0 and h>0 and i>0 and j>0 and k>0 and l>0 and m>0 and n>0 and o>0 and pp>0 and q>0 and r>0 and s>0 and a!=b and a!=c and a!=d and a!=e and a!=f and a!=g and a!=h and a!=i and a!=j and a!=k and a!=l and a!=m and a!=n and a!=o and a!=pp and a!=q and a!=r and a!=s and b!=c and b!=d and b!=e and b!=f and b!=g and b!=h and b!=i and b!=j and b!=k and b!=l and b!=m and b!=n and b!=o and b!=pp and b!=q and b!=r and b!=s and c!=d and c!=e and c!=f and c!=g and c!=h and c!=i and c!=j and c!=k and c!=l and c!=m and c!=n and c!=o and c!=pp and c!=q and c!=r and c!=s and d!=e and d!=f and d!=g and d!=h and d!=i and d!=j and d!=k and d!=l and d!=m and d!=n and d!=o and d!=pp and d!=q and d!=r and d!=s and e!=f and e!=g and e!=h and e!=i and e!=j and e!=k and e!=l and e!=m and e!=n and e!=o and e!=pp and e!=q and e!=r and e!=s and f!=g and f!=h and f!=i and f!=j and f!=k and f!=l and f!=m and f!=n and f!=o and f!=pp and f!=q and f!=r and f!=s and g!=h and g!=i and g!=j and g!=k and g!=l and g!=m and g!=n and g!=o and g!=pp and g!=q and g!=r and g!=s and h!=i and h!=j and h!=k and h!=l and h!=m and h!=n and h!=o and h!=pp and h!=q and h!=r and h!=s and i!=j and i!=k and i!=l and i!=m and i!=n and i!=o and i!=pp and i!=q and i!=r and i!=s and j!=k and j!=l and j!=m and j!=n and j!=o and j!=p and j!=q and j!=r and j!=s and k!=l and k!=m and k!=n and k!=o and k!=pp and k!=q and k!=r and k!=s and l!=m and l!=n and l!=o and l!=pp and l!=q and l!=r and l!=s and m!=n and m!=o and m!=pp and m!=q and m!=r and m!=s and n!=o and n!=pp and n!=q and n!=r and n!=s and o!=pp and o!=q and o!=r and o!=s and pp!=q and pp!=r and pp!=s and q!=r and q!=s and r!=s:
		
		print("")
		print("   ",a,b,c   )
		print("  ",d,e,f,g   )
		print(" ",h,i,j,k,l   )
		print("  ",m,n,o,pp   )
		print("   ",q,r,s   )
		print("")

print ("Time to solve: ", datetime.now() - startTime)