## Resources


<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Type/th>
  </tr>
</table>

##Named
GET /api/v1/{endpoint}/

###NamedAPIResourceList

## Pokemons
 /api/v1/pokemons/
## Pokemon
 /api/v1/pokemon/{pokemon name}
## Species
 /api/v1/species/
## Specie
 /api/v1/specie/{specie id}
## Types 
 /api/v1/types/
##EGgGroups
  /api/v1/egg-groups
##UserAgent
  /api/v1/history
##Stats
  /api/v1/stats
##USer
  /api/v1/user/{user name}
##Collections
  /api/v1/collections
##Collection
  /api/v1/collection/{collection name}
##Play
  /api/v1/play
##Potion
  /api/v1/potion
##PotionCollection
  /api/v1/potioncollection
##Abilities
GET /api/v1/abilities
####Parameters
<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Type/th>
  </tr>
  <tr>
    <th>pokemons</th>
    <th>effects</th>
    <th>limit</th>
    <th>offset</th>
    <th>unused</th>
    <th>generation</th>
    <th>query</th>
  </tr>  
  <tr>
    <th>when true shows the list of pokemons with this ability</th>
    <th>when true shows the list of effects of tha t abilitiey</th>
    <th>set limit to the number of abilities shwon</th>
    <th>start showing abilitiies list from the specified offset</th>
    <th> not implemented</th>
    <th>shows only abilities with that specified generation</th>
    <th>shows only abilities which contain that specific key</th>
  </tr>  
  <tr>
    <th>boolean</th>
    <th>boolean</th>
    <th>Integer</th>
    <th>Integer</th>
    <th>boolean</th>
    <th>boolean</th>
    <th>Text</th>
    <th>Text</th>
  </tr>
</table>
PUT /api/v1/abilities
####Required field
<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Type/th>
  </tr>
  
  <tr>
##Generation
  /api/v1/generations
