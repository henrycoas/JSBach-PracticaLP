\version "2.20.0" 
\score { 
	\new StaffGroup <<
		\new Staff \absolute { 
			\tempo 4 = 120 
			g' f' g' e' g' f' g' d' g' f' g' e' g' f' g' c' g' f' g' e' g' f' g' d' g' f' g' e' g' f' g' 
		} 
		\new Staff \absolute { 
			\tempo 4 = 120 
			r1 r8 g'4 f' g' e' g' f' g' d' g' f' g' e' g' f' g' c' g' f' g' e' g' f' g' d' g' f' g' e' g' f' g' 
		}
		\new Staff \absolute { 
			\tempo 4 = 120 
			r1 r4 g'4 f' g' e' g' f' g' d' g' f' g' e' g' f' g' c' g' f' g' e' g' f' g' d' g' f' g' e' g' f' g' 
		}
	>>
		\layout { } 
		\midi { } 
}