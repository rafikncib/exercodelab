console.log("Conexion between js and html has been done successufuly");

// Declaration of variables
var dictGame={
    start_game:false,
    tile_choosed:{tile:"",color:""},
    dictTiles:{
        tile1:{color:"",tileClicked:false},
        tile2:{color:"",tileClicked:false},
        tile3:{color:"",tileClicked:false},
        tile4:{color:"",tileClicked:false},
        tile5:{color:"",tileClicked:false},
        tile6:{color:"",tileClicked:false},
        tile7:{color:"",tileClicked:false},
        tile8:{color:"",tileClicked:false},
        tile9:{color:"",tileClicked:false},
        tile10:{color:"",tileClicked:false}
    },
    countDuplicate:0
}

const colors_array=["blue","red","yellow","black","purple"];

window.onload=function(){
    createGame();

    document.getElementById("tile1").addEventListener("click",function() {tilesfunction("tile1")});
document.getElementById("tile2").addEventListener("click",function() {tilesfunction("tile2")});

document.getElementById("tile3").addEventListener("click",function() {tilesfunction("tile3")});
document.getElementById("tile4").addEventListener("click",function() {tilesfunction("tile4")});
document.getElementById("tile5").addEventListener("click",function() {tilesfunction("tile5")});
document.getElementById("tile6").addEventListener("click",function() {tilesfunction("tile6")});
document.getElementById("tile7").addEventListener("click",function() {tilesfunction("tile7")});
document.getElementById("tile8").addEventListener("click",function() {tilesfunction("tile8")});
document.getElementById("tile9").addEventListener("click",function() {tilesfunction("tile9")});
document.getElementById("tile10").addEventListener("click",function() {tilesfunction("tile10")});


}


function createGame(){
    dictGame.start_game=false;
    dictGame.tile_choosed={tile:"",color:""};
        
    dictTilesCreate();
    for(let i=1;i<11;i++){
        //addColorTile(i)
        document.getElementById("tile"+i).style.backgroundColor="green";
    }
    console.log(dictGame.dictTiles);

}



function start(){
    document.getElementById("startButton").disabled =true;
    for(let i=1;i<11;i++){
        document.getElementById("tile"+i).style.backgroundColor="green";
    }
    dictTilesCreate();

    resetTileChoosed();
    dictGame.start_game=true;
    console.log("game start");
}

function reset(){
    //createGame();
    for(let i=1;i<11;i++){
        document.getElementById("tile"+i).style.backgroundColor="green";
    }
    resetTileChoosed();
    resetTileCliked();
    dictGame.start_game=true;
    console.log("game reset");
}

function timing(a,b){
    setTimeout(function(){
        console.log(a);
        document.getElementById(a).style.backgroundColor="green";
        document.getElementById(b).style.backgroundColor="green";
        dictGame.dictTiles[a].tileClicked=false;
        dictGame.dictTiles[b].tileClicked=false;
    },1500)
}

function tilesfunction(tile){
    if(!dictGame.start_game){
        console.log("game don't start yet");
        alert("Start the game !");
    }
    else if(!dictGame.dictTiles[tile]["tileClicked"]) 
    {
        document.getElementById(tile).style.backgroundColor=dictGame.dictTiles[tile].color;
        if(dictGame.tile_choosed.tile==""){
            dictGame.tile_choosed.tile=tile;
            dictGame.tile_choosed.color=dictGame.dictTiles[tile].color;
            console.log(dictGame.tile_choosed);
            dictGame.dictTiles[tile].tileClicked=true;
        }else{
            if(dictGame.tile_choosed.color===dictGame.dictTiles[tile].color){
                dictGame.countDuplicate += 1;
                console.log(dictGame.countDuplicate);
                if(dictGame.countDuplicate == colors_array.length){
                    dictGame.start_game =!dictGame.start_game;
                    alert(" You win, nice job!")
                    document.getElementById("startButton").disabled = false;
                }
                console.log("you did it");
                resetTileChoosed();
                dictGame.dictTiles[tile].tileClicked=true;
            }else{
                console.log("wrong wrong");
                timing(dictGame.tile_choosed.tile,tile);
                resetTileChoosed();
            }
        }
        
    }else{
        console.log("duplicate");
    }
}

function resetTileChoosed(){
    dictGame.tile_choosed.tile="";
    dictGame.tile_choosed.color="";
}

function resetTileCliked(){
    for(let i=1;i<11;i++){
        dictGame.dictTiles["tile"+i].tileClicked=false;
    }
}


function resetTileColor(){
    for(let i=1;i<11;i++){
        dictGame.dictTiles["tile"+i].color="";
    } 
}



function dictTilesCreate(){
    resetTileColor();
    for(let colorIndice = 0; colorIndice<colors_array.length ;colorIndice++){
        let countColor = 0;

        while(countColor < 2){
                let tileIndice = Math.floor((Math.random() * 10))+1;
                if(dictGame.dictTiles["tile"+tileIndice].color==""){

                    dictGame.dictTiles["tile"+tileIndice].color=colors_array[colorIndice];
                    dictGame.dictTiles["tile"+tileIndice].tileClicked=false;

                    console.log(tileIndice,dictGame.dictTiles["tile"+tileIndice].color);

                    countColor++;
                }
            }
    }
}

