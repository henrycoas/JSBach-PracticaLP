\version "2.20.0" 
\score { 
	\new StaffGroup <<
		\new Staff \absolute { 
			\tempo 4 = 120 
			r8 r8 r4 r4 g' g' f' f' g' g' e' e' g' g' f' f' g' g' d' d' g' g' f' f' g' g' e' e' g' g' f' f' g' g' c' c' g' g' f' f' g' g' e' e' g' g' f' f' g' g' d' d' g' g' f' f' g' g' e' e' g' g' f' f' g' g' 
		}
		\new Staff \absolute { 
			\tempo 4 = 120 
			r8 r4 a,,, b,,, c,, d,, e,, f,, g,, a,, b,, c, d, e, f, g, a, b, c d e f g a b c' d' e' f' g' a' b' c'' d'' e'' f'' g'' a'' b'' c''' d''' e''' f''' g''' a''' b''' c'''' d'''' e'''' f'''' g'''' a'''' b'''' 
		}
	>> 
	\layout { } 
	\midi { } 
}