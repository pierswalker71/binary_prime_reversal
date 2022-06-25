import streamlit as st

def main():
  
    # Import libraries
    import numpy as np # np can convert between numerical bases
    import pandas as pd
    import matplotlib.pyplot as plt

    #------------------------------------------------------------------
    # Settings
    st.set_page_config(page_title = 'binary_prime_reversal') 
    
    # Title
    st.title('Binary Prime Reversal Amazing Graph')
    st.write('Piers Walker 2022. https://github.com/pierswalker71')
    st.write('Generate the amazing graph presented in Numberphile video https://www.youtube.com/watch?v=pAMgUB51XZA at time 7:47')
    st.write('Sequence described by Neil Sloane, founder of The On-Line Encyclopedia of Integer Sequences: https://oeis.org/') 
    
    df = pd.DataFrame(data={'Prime':[2,3,5,7,11,13,17,19,25], 'Binary':['10','11','101','111','1011','1101','10001','10011','10111'],
                            'Backward':['01','11','101','111','1101','1011','10001','11001','11101'],
                            'Results':[1,0,0,0,-2,2,0,-6]})
    
    
    st.write('the process to generate the values is...')
    st.write('Example table showing the first few primes')
    st.dataframe(df)

    #------------------------------------------------------------------

    # Define functions
    def generate_primes(min,max):
       # Returns a list of primes between the min and max limits
        prime_num_list = []
        for num in range(min,max+1):
            if num>1:
                for a in range(2,num):
                    if (num % a) == 0:
                        break
                else: 
                    prime_num_list.append(num)

        return(prime_num_list)

    def reverse(num):
      # Reverses a string
        num_rev_list = list(reversed(str(num)))
        num_rev = int("".join(num_rev_list))

        return(num_rev)

    #------------------------------------------------------------------
    # User setings 
    max_num = st.number_input('maximum prime number (2 - 30000)', min_value=2, max_value=30000, value=10000) 
       
    colours = {'red':'r','blue':'b','green':'g','yellow':'y','black':'k'}
    markers = {'point':'.', 'circle':'o', 'star':'*', 'cross':'x'}
       
    markersize = st.number_input('marker size (0.01 - 10.0)', min_value=0.01, max_value=10.0, value=0.5) 
    colour = st.selectbox('colour', [x for x in colours.keys()])
    marker = st.selectbox('shape', [x for x in markers.keys()])
    
    marker = colours[colour] + markers[marker]

    #------------------------------------------------------------------
    # Create list of primes
    prime_num_list = generate_primes(1,max_num)

    # Convert decimal to binary
    binary_num_list = []
    for p in range(0,len(prime_num_list)):
        binary_num_list.append(int(np.binary_repr(prime_num_list[p])))

    # Reverse binary values
    reverse_binary_num_list = []
    for b in range(0,len(prime_num_list)):
        reverse_binary_num_list.append(reverse(binary_num_list[b]))

    # Convert binary to decimal.  int(str(1101),2) converts from base 
    dec_reverse_binary_num_list = []
    for d in range(0,len(prime_num_list)):
        dec_reverse_binary_num_list.append(int(str(reverse_binary_num_list[d]),2))

    # Calculate result
    result = list(np.array(prime_num_list)- np.array(dec_reverse_binary_num_list))
    
    #------------------------------------------------------------------
    # Plot results
    fig,ax = plt.subplots(figsize=(15,6))

    ax.plot(prime_num_list,result, marker, markersize=markersize)

    ax.set(xlabel='Primes',ylabel='Result') 
    ax.set_title(f'Result for Max Prime of {max_num}', weight='bold',size=14)
    ax.tick_params(axis='x',labelsize=14)
    ax.tick_params(axis='y',labelsize=12)
    ax.xaxis.label.set_fontsize(15)
    ax.yaxis.label.set_fontsize(15)
    ax.grid()
    
    st.pyplot(fig)
    
    
if __name__ == '__main__':
    main()
