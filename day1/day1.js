var beersong = {
    
    firstline: function(id){

        var idStr = id;
        if (id===0) 
            idStr = "No more";

        var l = idStr + " bottle" + (id == 1 ? '' : 's') + " of beer";
        var out = l + " on the wall, " + l + "."
        return out;
    },

    secondline: function(id){

        var v = id + "bottle" +  + "of beer on the wall, "
            + id 
            + " bottle" + (id == 1 ? '' : 's') 
            + " of beer."


    },

    verse: function(id){

        console.log( firstline(id) + "\n" + secondline(id) )

    }


}

console.log(beersong.firstline(2));
console.log(beersong.firstline(1));
console.log(beersong.firstline(0));