# Count inversions of an array.
count = 0 
def count_sort(arr , begin , end):
    mid = (begin+end) // 2
    if begin >= end:
        return
    count_sort(arr , begin , mid)
    count_sort(arr , mid+1 , end)
    merge(arr , begin , mid , end)
    
def merge(arr , begin , mid , end):
    i = begin
    j = mid+1
    b = []
    while ( i <= mid or j <= end):
        if i > mid :
            b.extend(arr[j:end+1])
            break
        elif j > end:
            b.extend(arr[i:mid+1])
            break
        elif arr[i] <= arr[j]:
            b.append(arr[i])
            i+=1
        else:
            b.append(arr[j])
            j+=1
            global count
            count += mid - i + 1
    arr[begin:end+1] = b
if __name__ == "__main__":
    
    with open( 'nums.txt' , 'r' ) as file :
        lines = file.readlines()
    nums = [ int(i.strip()) for i in lines ]
    count_sort(nums , 0 , len(nums)-1 )
    
    print(count)
