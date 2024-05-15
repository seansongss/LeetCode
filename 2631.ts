declare global {
    interface Array<T> {
        groupBy(fn: (item: T) => string): Record<string, T[]>
    }
}

Array.prototype.groupBy = function(fn) {
    const result = {};
    for (let i of this){
        if (!(fn(i) in result)) result[fn(i)] = [];
        result[fn(i)].push(i);
    }
    return result;
}

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */