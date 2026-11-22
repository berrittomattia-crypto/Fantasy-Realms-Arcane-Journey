// Fantasy Realms - God Wand progression gate
// The only player crafting recipe shipped by God Wand is removed here.
// The item is granted as the final FTB Quests reward in "Il potere assoluto".
ServerEvents.recipes(event => {
  event.remove({ output: 'godwand:god_wand' })
  console.info('[Fantasy Realms] Removed the God Wand crafting recipe; final quest reward only.')
})
