export default function hasValueFromArray(s, arr) {
 for (const value of arr) {
    if (!s.has(value))
        return false;
 }
 return true;
}