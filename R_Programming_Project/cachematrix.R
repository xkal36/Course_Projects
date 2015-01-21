# We wish to compute the inverse of a square matrix. This can be quite time
# consuming, so we need to cache the inverse. The first function below creates
# a matrix that supports caching, while the second operates on that to get the
# inverse. It first checks wheteher we have already cached the result. If so,
# it simply retrieves and returns that value. If not, it computes it directly,
# adds it to the cache, then returns the value.


# Creates a special 'matrix' object that can cache its inverse.
makeCacheMatrix <- function(x = matrix()) {
    inv <- NULL
    set_mat <- function(y) { # sets the value of the matrix
        x <<- y
        inv <<- NULL
    }
    get_mat <- function() x # gets the matrix
    set_inv <- function(solve) inv <<- solve # sets the inverse
    get_inv <- function() inv # gets the inverse
    list(set_mat = set_mat, get_mat = get_mat,
         set_inv = set_inv, get_inv = get_inv)
}


# Gets and returns the inverse of x, either from the cache if in it, 
# else by computing it directly, then adding it to the cache before returning.
cacheSolve <- function(x, ...) {
    inv <- x$get_inv() # gets the inverse
    if(!is.null(inv)) { # ie if the inv is already in the cache
        message("Getting inverse from the cache!")
        return(inv)
    }
    # If not in the cache, we compute it, add to cache, and return the inverse
    data <- x$get_mat() 
    inv <-solve(data, ...)
    x$set_inv(inv)
    inv
}
