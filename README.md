# Scratchbit

This is a micropython script for micro:bit made by **Ákos Vecsei**

With this script you can use your micro:bit as a Scratch *(developed by MIT)* controller.

### [DEMO VIDEO](https://www.youtube.com/watch?v=F8J47OMNxso&t=42s)

## What do you need?

A **micro:bit** with **USB cable**.

## How can you install it?

1. Clone this repo or simple download the scratchbit.py script:

	```
	git clone https://github.com/vecsei/Scratchbit.git
	```
	So now you have the `scratchbit.py` inside the `Scratchbit` folder

2. Flash it to the micro:bit.

3. Start [Scratch](http://scratch.mit.edu)

4. Add the built-in `PicoBoard extension`.

5. When "C" is displayed on the micro:bit, the connection was established.

6. You can use the `scratchbitdemo.sb2` to try it.


## How can you use it?

- The `resistance-A` in Scratch represents the `press of the "A" button` on the micro:bit.

- The `resistance-B` in Scratch represents the `press of the "B" button` on the micro:bit.

- The `resistance-C` in Scratch represents the `X direction tilt` of the micro:bit.

- The `resistance-D` in Scratch represents the `Y direction tilt` of the micro:bit.

- The `light` in Scratch represents the value of the micro:bit's `P0 pin`.

- The `sound` in Scratch represents the value of the micro:bit's `P1 pin`.

- The `slider` in Scratch represents the value of the micro:bit's `P2 pin`.

|    Scratch   |        micro:bit        |
|:------------:|:-----------------------:|
| resistance-A | press of the "A" button |
| resistance-B | press of the "B" button |
| resistance-C |     X direction tilt    |
| resistance-D |     Y direction tilt    |
|     light    |          P0 pin         |
|     sound    |          P1 pin         |
|    slider    |          P2 pin         |

