def maxHeapify(array, size, k):
  # Initially assume that the largest value of the node and its children is the node itself (i.e. heap structure is satisfied)
  largest = k
  
  # Define the indices of the left and right children based on the heap structure
  i_left = leftIndex(k)
  i_right = rightIndex(k)
  
  # If the node has a left index and its value is greater than the node, set the index of the largest value to the left child
  if i_left < size and array[i_left] > array[largest]:
    largest = i_left
    
  # If the node has a right index and its value is greater than the node or the left index, set the index of the largest value to the right child
  if i_right < size and array[i_right] > array[largest]:
    largest = i_right

  # If on of the children has a value larger than the node, swap the indices to restore the max heap structure and repeat the heaping exercise for the node in its new child position
  if k != largest:
    array[k], array[largest] = array[largest], array[k]
    maxHeapify(array, size, largest)
    
def minHeapify(array, size, k):
  # Initially assume that the largest value of the node and its children is the node itself (i.e. heap structure is satisfied)
  smallest = k
  
  # Define the indices of the left and right children based on the heap structure
  i_left = leftIndex(k)
  i_right = rightIndex(k)
  
  # If the node has a left index and its value is greater than the node, set the index of the largest value to the left child
  if i_left < size and array[i_left] < array[smallest]:
    smallest = i_left
    
  # If the node has a right index and its value is greater than the node or the left index, set the index of the largest value to the right child
  if i_right < size and array[i_right] < array[smallest]:
    smallest = i_right

  # If on of the children has a value larger than the node, swap the indices to restore the max heap structure and repeat the heaping exercise for the node in its new child position
  if k != smallest:
    array[k], array[smallest] = array[smallest], array[k]
    minHeapify(array, size, smallest)
  
def leftIndex(k):
    return 2*k + 1
  
def rightIndex(k):
    return 2*k + 2

# Go through all nodes in the tree and make sure their children satisfy the max heap property
def maxHeap(array, size):
    # We're only interested in nodes (not leaves) since leaves implicitly satisfy max heap property by having no children. Therefore, only consider elements of nodes
    i_max_node = size // 2 - 1
    for i in range(i_max_node + 1):
        k = size // 2 - i - 1
        maxHeapify(array, size, k)

# Go through all nodes in the tree and make sure their children satisfy the min heap property
def minHeap(array, size):
    # We're only interested in nodes (not leaves) since leaves implicitly satisfy max heap property by having no children. Therefore, only consider elements of nodes
    i_max_node = size // 2 - 1
    for i in range(i_max_node + 1):
        k = size // 2 - i - 1
        minHeapify(array, size, size//2-i-1)

def insert_maxHeap(array, size, value):
    # If there's no node, create one
    if len(array) == 0:
        array = [value]
    else:
        array.append(value)
        maxHeap(x, size+1)
    return size+1

def insert_minHeap(array, size, value):
    # If there's no node, create one
    if len(array) == 0:
        array = [value]
    else:
        array.append(value)
        minHeap(x, size+1)
    return size+1
    
def delete_maxHeap(array, size, value):
    i_first_leaf = size // 2
    # First check if the value to delete is a leaf
    for k in range(i_first_leaf, size):
        if array[k] == value:
            del array[k]
            maxHeap(array, size-1)
            return size-1
    for k in range(i_first_leaf):
        if array[k] == value:
            # Swap the value with the last leaf and remove it
            array[k], array[-1] = array[-1], array[k]
            del array[-1]
            
            # Max heapify the array
            maxHeap(array, size-1)
            return size-1
    return size-1
    
def delete_minHeap(array, size, value):
    i_first_leaf = size // 2
    # First check if the value to delete is a leaf
    for k in range(i_first_leaf, size):
        if array[k] == value:
            del array[k]
            minHeap(array, size-1)
            return size-1
    for k in range(i_first_leaf):
        if array[k] == value:
            # Swap the value with the last leaf and remove it
            array[k], array[-1] = array[-1], array[k]
            del array[-1]
            
            # Min heapify the array
            minHeap(array, size-1)
            return size-1
    return size-1
            
x = [3,9,2,1,4,5]
maxHeap(x, len(x))
print(x)
size = insert_maxHeap(x, len(x), 10)
print(x)
size = delete_maxHeap(x, size, 2)
print(x)

minHeap(x, len(x))
print(x)
size = insert_minHeap(x, size, 7)
print(x)
size = delete_minHeap(x, size, 1)
print(x)


