# state-thoughts

A writeup of my thoughts on the current state model

## Todo

- Then put together the second example
- Look for more examples from the state example
- Write up my notes on why I did what I did
- Write up general principles I think are important for 
    - state
    - something to be "streamlit-y"
    - Why I no longer think we need state to be as carefully protected as
      before
- Read the objection doc they wrote. Write in my own thoughts
- Write an intro basically
    - We want to find the solution which makes the *most sense* to our users
    - We want to make it possible to write apps in the style of 
      data-transformation-like Python scripts
    - We want to use state as sparingly as possible
- See if I have time to code up the DONT_CHANGE constant

## Examples

- Errors before and after 
- closures
- sliders that re-initialize the state

## Questions

- Can state be instantiated with two separate places?

## Why does `st_event` work the way it does?

- The **context** is included so that you an create continuations
- The **DONT_CHANGE** object is included so that you can avoid changing
  the value of an object.

## Notes

- I wonder if there's a way we can do signal handling at the bottom of the 
  script? (Without getting off-by-one errors?)
  
- Two similar concepts are (1) global variables in imported packages, and (2)
  state. They have similar enough semantics (aka they stay around between runs)
  that you might use them intergchangeably. (I did in st_event.py.) But they
  don't reset at the same time, which can be the source of subtle bugs.

- **There's something to be figured out about how to do the interaction with
  auto-reload and state initialization.** For example, maybe if the state
  intialization code changes, the state needs to be reset? Or maybe when the
  code auto-reloads, it should indicate with a toast that it's resuing the
  previous state, and then offer the ability to click to reset the state.

- I feel like callbacks have a way of taking over the whole script and forcing
  the user to resort to a mode where the entire state of the script is
  encapsulated by the state. Is that really what we want?

- In general, there's a big issue if `st.beta_session_state()` is called in two
  different parts of the code becuase they may not initialize the same values.

