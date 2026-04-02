var expect = function (actual) {
    let tne = () => { throw new Error("Not Equal") };
    let te = () => { throw new Error("Equal") };

    return {
        toBe: (v) => v === actual || tne(),
        notToBe: (v) => v !== actual || te(),
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
