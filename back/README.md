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

####Required field
<table style="width:100%">
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Type</th>
  </tr>
  
  <tr>
    <th>name</th>
    <th>the name of the new ability</th>
    <th>text</th>
  </tr>
  
  <tr>
    <th>generation</th>
    <th>the generation of this ability</th>
    <th>text</th>
  </tr>
</table>


##Generation
GET /api/v1/generations
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
