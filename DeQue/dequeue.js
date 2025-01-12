class Deque{ 
	/**
	 * 
	 * @param {*} size 
	 */
	constructor(size){ 
		this.bucket = new Array(size).fill(null)
		this.front = size - 1
		this.rear = size - 1 
	}
					
	//               fr 
	// [null, 1, null]   	
	append_rear = (num) => {
		this.rear = (this.rear + 1) % this.bucket.length // move rear forward
		this.bucket[this.rear] = num
	}
	pop_rear = () => { 
		this.bucket[this.rear] = null  
		this.rear = (this.rear - 1) % this.bucket.length 
	}

	append_front = (num) => { 
		this.front = (this.front - 1) % this.bucket.length
		this.bucket[this.front] = num
	}
	pop_front = () => { 
		this.bucket[this.front] = null 
		this.front = (this.front + 1 ) % this.bucket.length
	}	
}