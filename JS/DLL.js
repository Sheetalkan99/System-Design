class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

class DLL {
    constructor(val) {
        const newNode = new Node(val); // Fixed initialization
        this.head = newNode;
        this.tail = this.head;
        this.length = 1;
    }

    print() {
        let temp = this.head;
        let result = [];
        while (temp) {
            result.push(temp.val);
            temp = temp.next;
        }
        console.log(result.join(" <-> "));
    }

    push(val) {
        const newNode = new Node(val);
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }
        this.length++;
        return this;
    }
    pop(val){
        if(!this.head){
            return null
        }
        if(this.length === 1){
            this.head = null
            this.tail = null;;
        }
        else{
            let temp = this.tail 
            this.tail = this.tail.prev
            this.tail.next = null
            temp.prev = null
            this.length--
            return this
        }
    }
    unshift(val){
        const newNode  = new Node(val)
        if(this.length === 0){
            this.head = newNode
            this.tail = newNode
        }
        newNode.next = this.head
        this.head.prev = newNode
        this.head = newNode
        this.length ++
        return this
    }

    shift(){
       this.head = this.head.next 
       this.head.prev = null
       this.length --
       return this
    }

    get(index){
        if(index < 0 || index >= this.length) return undefined
        let temp = this.head
        if(index < this.length/2){
            for( let i = 0; i < index; i ++){
                temp = temp.next
            }
            }else
            {
                temp = this.tail 
                for(let i = this.length- 1; i > index; i --){
                    temp = temp.prev
                }
        }
        return temp
    }

    set(index, val){
        let temp = this.get(index)
        //const newNode = new Node(val)
        if(temp){
            temp.val = val;
            return true
        }
        return false

    }

    insert(index, val){
        
        const newNode = new Node(val)
        if(index === 0){
            return this.unshift(val);
        }
        if(index === this.length){
            this.push(val)
        }
        let before= this.get(index - 1)
        let after = before.next 
        before.next = newNode
        newNode.prev = before
        newNode.next = after
        after.prev = newNode

        this.length++
        return this


    }

    remove(index) {
        if (index < 0 || index >= this.length) return undefined; // Out-of-bounds check
        
        if (index === 0) return this.shift(); // Remove first element
        if (index === this.length - 1) return this.pop(); // Remove last element
        
        let temp = this.get(index);
        if (!temp) return undefined; // If get() fails, return undefined
    
        temp.prev.next = temp.next;
        temp.next.prev = temp.prev;
        
        temp.next = null;
        temp.prev = null;
        
        this.length--;
        return temp; // Return removed node
    }
    
    swapfl(){
        if(this.length < 2){
            return 
        }else{
            let temp = this.head.val
            this.head.val = this.tail.val
            this.tail.val = temp

            return this
            
        }
    }

    rev(){
        if(this.length< 0 ){return}
            let curr = this.head 
            let temp = null
            while(curr !== null){
                temp = curr.prev
                curr.prev = curr.next 
                curr.next = temp
                curr = curr.prev
            }
            temp = this.head
            this.head = this.tail 
            this.tail = temp
            return this        
            
      
    }
    detectcyc(){
        slow = this.head
        fast = this.head.next
        while(fast !== null && fast.next !== null){
            slow = slow.next
            fast = fast.next.next
            if(slow === fast){
                return true
            }else{return false}
            
        }
    }

    palindrome() {
        if (!this.head || this.length <= 1) return true; // Empty or single-node list is a palindrome
    
        let forward = this.head;
        let backward = this.tail;
    
        for (let i = 0; i < Math.floor(this.length / 2); i++) {
            if (forward.val !== backward.val) {
                return false;
            }
            forward = forward.next;
            backward = backward.prev;
        }
    
        return true;
    }
    



}

// Testing
let first = new DLL(20);

first.push(30);
first.push(30);
first.push(20);
/*
first.pop(); 
first.unshift(90);
first.shift()
console.log(first.get(2));
first.set(1, 44);
first.print();
first.insert(2,66)
first.remove(1)
first.print();
first.swapfl();
*/

console.log(first.palindrome())

first.print()