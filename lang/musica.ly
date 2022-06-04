\version "2.20.0" 
\score { 
	\new StaffGroup <<
		\new Staff \absolute { 
			\tempo 4 = 120 
			r8 r4 g' f' g' e' g' f' g' d' g' f' g' e' g' f' g' c' g' f' g' e' g' f' g' d' g' f' g' e' g' f' g' 
		}
		\new Staff \absolute { 
			\tempo 4 = 120 
			a,,, b,,, c,, d,, e,, f,, g,, a,, b,, c, d, e, f, g, a, b, c d e f g a b c' d' e' f' g' a' b' c'' d'' e'' f'' g'' a'' b'' c''' d''' e''' f''' g''' a''' b''' c'''' d'''' e'''' f'''' g'''' a'''' b'''' 
		}
	>> 
	\layout { } 
	\midi { } 
}