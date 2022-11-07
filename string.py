## Question 3 
 

def return_two_integers(A, B):
 #initialize empty string variable 
    rt = ""
    while (0 < A or 0 < B) :
 
        # More 'b', append "bba"
        if (A < B) :
            if (0 < B):
                rt = rt +'b'
                B -= 1
            if (0 < B):
                rt += 'b'
                B -= 1
            if (0 < A):
                rt += 'a'
                A -= 1
 
        # More 'a', append "aab"
        elif (B < A):
            if (0 < A):
                rt += 'a'
                A -= 1
            if (0 < A):
                rt += 'a'
                A -= 1
            if (0 < B):
                rt += 'b'
                B -= 1
 
       
        else :
            if (0 < A):
                rt += 'a'
                A -= 1
            if (0 < B):
                rt += 'b'
                B -= 1
    print(rt)
 
# Driver code
if __name__ == "__main__":
     #default values 
    A = 5
    B = 3
    return_two_integers(A, B)
           

