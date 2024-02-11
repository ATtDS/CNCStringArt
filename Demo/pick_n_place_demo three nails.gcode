G21 ; Set units to millimeters
G90 ; Absolute positioning

; Move to pick-up location (X278 Y109)
G0 Z-1 ; Raise Z to a safer height
G0 X278 Y109
G1 Z-20 F500 ; Lower to pick-up height
; (Here the machine would pick up a nail)

; Move to first placement location (X93 Y192)
G0 Z-1 ; Raise Z before moving
G0 X93 Y192
G1 Z-31 F500 ; Lower to placement height
; (Here the machine would place the nail)

; Repeat for second nail, 20mm below the first
G0 Z-1 ; Raise Z before moving
G0 X278 Y109 ; Back to pick-up location
G1 Z-20 F500 ; Lower to pick-up height
; (Pick up second nail)

G0 Z-1 ; Raise Z before moving
G0 X278 Y120 
G0 X93 Y172 ; Move to second placement location (20mm below first)
G1 Z-31 F500 ; Lower to placement height
; (Place second nail)

; Repeat for third nail, 20mm below the second
G0 Z-1 ; Raise Z before moving
G0 X278 Y109 ; Back to pick-up location
G1 Z-20 F500 ; Lower to pick-up height
; (Pick up third nail)

G0 Z-1 ; Raise Z before moving
G0 X278 Y120 
G0 X93 Y152 ; Move to third placement location (20mm below second)
G1 Z-31 F500 ; Lower to placement height
; (Place third nail)
