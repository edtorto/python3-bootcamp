from replit import clear
# function for auction
def secret_auction():
    print("Welcome to the secret auction program.")
    bids = {}
    bidding_finished = False

    while not bidding_finished:
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        bids[name] = bid

        should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        if should_continue == 'no':
            bidding_finished = True
            clear()
        else:
            clear()

    highest_bidder = max(bids, key=bids.get) # type: ignore
    print(f"The winner is {highest_bidder} with a bid of ${bids[highest_bidder]}")

# calling the function   
if __name__ == "__main__":
    secret_auction() # type: ignore