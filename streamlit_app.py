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
    st.title('Graph of "Binary Prime Reversal" Sequence')
    st.write('Piers Walker 2022. https://github.com/pierswalker71')
    st.write('Generate the amazing graph presented in Numberphile video https://www.youtube.com/watch?v=pAMgUB51XZA at time 7:47')
    st.write('Sequence described by Neil Sloane, founder of The On-Line Encyclopedia of Integer Sequences: https://oeis.org/')    
    
    st.markdown('The process to generate the values comprises the following steps:<br> \
             1) Generate a list of prime numbers.<br> \
             2) Convert the primes into their binary equivalient.<br>\
             3) Reverse the order of the binary characters.<br>\
             4) Convert these reversed binary numbers back to decimals.<br>\
             5) Subtract these reversed numbers from the original prime numbers.<br>\
             6) Plot the two sets of values')
    
    st.write('Example table showing the first few primes')
    df = pd.DataFrame(data={'Prime':[2,3,5,7,11,13,17,19], 'Binary':['10','11','101','111','1011','1101','10001','10011'],
                           'Backward':['01','11','101','111','1101','1011','10001','11001'],
                            'Results':[1,0,0,0,-2,2,0,-6]})
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
    st.subheader('Settings')
    max_num = st.number_input('maximum prime number (2 - 30000)', min_value=2, max_value=30000, value=10000) 
       
    colours = {'red':'r','blue':'b','green':'g','yellow':'y','black':'k'}
    markers = {'point':'.', 'circle':'o', 'star':'*', 'cross':'x'}
       
    markersize = st.number_input('marker size (1 - 10)', min_value=1, max_value=10, value=5) 
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
    st.subheader('Output')
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
