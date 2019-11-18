## Resources
<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Type</th>
  </tr>
</table>

##Named
GET /api/v1/{endpoint}


<br><br/>
###NamedAPIResourceList:
<br><br/>
## Pokemons
GET /api/v1/pokemons
####Description
Get the list of pokemons with their stats

####Parameters
<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Type</th>
  </tr>
  <tr>
    <th>query</th>
    <th>Optional argument: filter the pokemons with the query in their name</th>
    <th>text</th>
  </tr> 
   <tr>
    <th>type</th>
    <th>Optional argument: when a type is specified filter the pokemons of that type</th>
    <th>text</th>
  </tr> 
   <tr>
    <th>filter_ability</th>
    <th>Optional argument: when an ability is specified filter the pokemons of that ability</th>
    <th>text</th>
  </tr>
   <tr>
    <th>effect</th>
    <th>Optional argument: when true for each pokemons it is shows its effects</th>
    <th>boolean</th>
  </tr>
   <tr>
    <th>show_abilities</th>
    <th>Optional argument: when true for each pokemons it is shows its abilities</th>
    <th>boolean</th>
  </tr>
</table>

<br><br/>
POST /api/v1/pokemons
####Description
Insert a new pokemon in the database
####Required field
{name: pokemon_name,
hp: pokemon_hp}
<br><br/>
## Pokemon

GET /api/v1/pokemon/{pokemon name}
####Description
Return the stats of the specific pokemon
####Parameters
<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Type</th>
  </tr>
   <tr>
    <th>shape</th>
    <th>Optional argument: when true it return also the shapes of the pokemon</th>
    <th>boolean</th>
  </tr>
  </table>
<br><br/>
PATCH /api/v1/pokemon/{pokemon name}

####Description
Allow to edit the pokemon stats
####Required field
Specifying the stats of the pokemon to be modified with their new value

<br><br/>
DELETE /api/v1/pokemon/{pokemon name}
####Description
Delete the pokemon from the database


## Species
GET /api/v1/species
####Description
Get the list of the species
####Parameters
<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Type</th>
  </tr>
  <tr>
    <th>pokemons</th>
    <th>Optional argument: shows the name of the pokemons for each specie</th>
    <th>text</th>
  </tr>
  <tr>   
    <th>egggroup</th>
    <th>Optional argument: when true the eggo group  are shown for each specie</th>
    <th>boolean</th>
  </tr>
  <tr>   
    <th>limit</th>
    <th>Optional argument: specify the maximum number of species shown; default is 3</th>
    <th>Integer</th>
  </tr>
</table>


<br><br/>
PUT /api/v1/species
####Description
Associate a pokemon to a specie
####Required field
{specie: specie,
pokemon: pokemon,
is_default: is_default}


## Specie
GET /api/v1/specie/{specie id}
####Description
Get the detais of one specie with the name of the pokemons associated

## Types 
GET /api/v1/types/
####Description
Get the list of types
####Parameters
<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Type</th>
  </tr>
  <tr>
    <th>pokemons</th>
    <th>Optional argument: when true shows the pokemons for each type</th>
    <th>booblean</th>
  </tr>
  <tr>   
    <th>unused</th>
    <th>Optional argument: when true shows the types not used</th>
    <th>boolean</th>
  </tr>
  <tr>   
    <th>query</th>
    <th>Optional argument: filter the list of types</th>
    <th>text</th>
  </tr>
</table>

PUT /api/v1/types/
####Description
Add a new type to the database
####Required fields
{name: name,
generation: generation}

##EGgGroups
  /api/v1/egg-groups
####Description


##UserAgent
  /api/v1/history
####Description  
 
##Stats
GET /api/v1/stats

####Description
Return the average value of that stat over all the pokemons
##User
  /api/v1/user/{user name}
####Description


##Collections
  /api/v1/collections
####Description


##Collection
  /api/v1/collection/{collection name}
####Description
  
##Play
  /api/v1/play
####Description

##Potion
  /api/v1/potion
####Description

##PotionCollection
  /api/v1/potioncollection
####Description

##Abilities
GET /api/v1/abilities
####Description

####Parameters
<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Type</th>
  </tr>
  
  <tr>
    <th>pokemons</th>
    <th>when true shows the list of pokemons with this ability</th>
    <th>boolean</th>
  </tr>
  
  <tr>
    <th>effects</th>
    <th>when true shows the list of effects of that ability</th>
    <th>boolean</th>
  </tr>
  
  <tr>
    <th>limit</th>
    <th>set limit to the number of abilities shown</th>
    <th>Integer</th>
  </tr>
  
  <tr>
    <th>offset</th>
    <th>set limit to the number of abilities shwon</th>
    <th>Integer</th>
  </tr>
  
  <tr>
    <th>unused</th>
    <th>not implemented</th>
    <th>not applicable</th>
  </tr>

  <tr>
    <th>generation</th>
    <th>shows only abilities with that specified generation</th>
    <th>text</th>
  </tr>

  <tr>
    <th>query</th>
    <th>shows only abilities which contain that specific key</th>
    <th>text</th>
  </tr>
</table>


PUT /api/v1/abilities
####Description

####Required field


{name: new_name,
generation: generation_associated}


##Generation
GET /api/v1/generations
####Description
####Parameters
<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Type</th>
  </tr>
  
  <tr>
    <th>query</th>
    <th>when true shows the list of pokemons with this ability</th>
    <th>boolean</th>
  </tr>
  
  <tr>
    <th>ability_number</th>
    <th>when true shows the list of effects of that ability</th>
    <th>boolean</th>
  </tr>
  
  <tr>
    <th>type_number</th>
    <th>set limit to the number of abilities shown</th>
    <th>Integer</th>
  </tr>
</table>

PUT /api/v1/generations
####Description
Add a new generation to the database
####Parameters
<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Type</th>
  </tr>
  
  <tr>
    <th>generation</th>
    <th>The name of the new generation</th>
    <th>text</th>
  </tr>
</table>


