# 4.13 hot potato

from collections import deque

def hot_potato(players, num_passes):
  queue = deque(players) # Create a queue from the list of players
  
  while len(queue) > 1: # Continue until only one player is left
    for _ in range(num_passes):
      # Pass the potato 'num_passes' times
      queue.append(queue.popleft()) # Move the front player to the back
    
    # Eliminate the player holding the potato
    eliminated_player = queue.popleft()  # Remove the player at the front
    print(f"{eliminated_player} has been eliminated.")
    
    # The last remaining player
    return queue.popleft()

# Example usage
players = ["Alice", "Bob", "Charlie", "David", "Eve"]
num_passes = 7
winner = hot_potato(players, num_passes)
# print(f"The winner is {winner}.")
