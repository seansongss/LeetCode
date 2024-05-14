function* fibGenerator(): Generator<number, any, number> {
    let pprev: number = 0;
    let prev: number = 1;
    let current: number = 1;
    yield 0;
    yield prev;
    yield current;
    while (true) {
        pprev = prev;
        prev = current;
        current = pprev + prev;
        yield current;
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
