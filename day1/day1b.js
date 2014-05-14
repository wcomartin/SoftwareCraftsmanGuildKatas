var beersong = {

    verse: function(id){

        if (id > 1){

            return id + " bottles of beer on the wall, " + id + " bottles of beer."+
            "\nTake one down and pass it around, " + (id - 1) + " bottles of beer on the wall";

        } else if (id == 1){

            return id + " bottle of beer on the wall, " + id + " bottle of beer."+
            "\nTake one down and pass it around, no more bottles of beer on the wall"

        } else {

            return "No more bottles of beer on the wall, no more bottles of beer."+
            "\nGo to the store and buy some more, 99 bottles of beer on the wall"

        }

    },

    sing: function(from, to){

        for (var i = from; i >= to; i--){

            console.log(this.verse(i) + "\n");

        }

    }

}

Hello my name is william comartin


beersong.sing(8,2);

console.log("\n\n\n\n\n\n")

console.log(beersong.verse(2));
console.log(beersong.verse(1));
console.log(beersong.verse(0))
;