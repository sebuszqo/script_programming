const fs = require('fs');

// exportuje funkcje aby użyć jej w script.js

exports.isDirOrFile = (fileOrDirectory) => {
    try {
        const stat = fs.statSync(fileOrDirectory);
        if (stat.isFile()) {
            console.log(`${fileOrDirectory} jest plikiem, a jego zawartością jest:`);
            return (fs.readFileSync(fileOrDirectory, 'utf-8'));
        } else if (stat.isDirectory()) {
            return (`${fileOrDirectory} jest katalogiem`);
        } else {
            return (`${fileOrDirectory} to coś innego`);
        }
    } catch (error) {
        return (`Nie udało się odczytać informacji o pliku lub katalogu: ${error}`);
    }
}

// console.log(isDirOrFile(argv[2]))