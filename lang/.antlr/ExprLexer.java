// Generated from /home/henry/Repos/PracticaLP-JSBach/lang/Expr.g by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ExprLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ASSIGN=1, EQ=2, NEQ=3, GT=4, LT=5, GE=6, LE=7, PLUS=8, MINUS=9, MUL=10, 
		DIV=11, MOD=12, READ=13, WRITE=14, REPRO=15, IF=16, ELSE=17, WHILE=18, 
		CONCAT=19, CUT=20, LPAREN=21, RPAREN=22, DIGIT=23, LETTER=24, NUMBER=25, 
		ID=26, STRING=27, WS=28;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"ASSIGN", "EQ", "NEQ", "GT", "LT", "GE", "LE", "PLUS", "MINUS", "MUL", 
			"DIV", "MOD", "READ", "WRITE", "REPRO", "IF", "ELSE", "WHILE", "CONCAT", 
			"CUT", "LPAREN", "RPAREN", "DIGIT", "LETTER", "NUMBER", "ID", "ESC_SEQ", 
			"STRING", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'<-'", "'='", "'/='", "'>'", "'<'", "'>='", "'<='", "'+'", "'-'", 
			"'*'", "'/'", "'%'", "'<?>'", "'<!>'", "'<:>'", "'if'", "'else'", "'while'", 
			"'<<'", "'8<'", "'|:'", "':|'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ASSIGN", "EQ", "NEQ", "GT", "LT", "GE", "LE", "PLUS", "MINUS", 
			"MUL", "DIV", "MOD", "READ", "WRITE", "REPRO", "IF", "ELSE", "WHILE", 
			"CONCAT", "CUT", "LPAREN", "RPAREN", "DIGIT", "LETTER", "NUMBER", "ID", 
			"STRING", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public ExprLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Expr.g"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\36\u00a4\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\3\2\3\2\3\2\3"+
		"\3\3\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n"+
		"\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17"+
		"\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23"+
		"\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27"+
		"\3\27\3\27\3\30\3\30\3\31\3\31\3\32\6\32\u0085\n\32\r\32\16\32\u0086\3"+
		"\33\3\33\3\33\7\33\u008c\n\33\f\33\16\33\u008f\13\33\3\34\3\34\3\34\3"+
		"\35\3\35\3\35\7\35\u0097\n\35\f\35\16\35\u009a\13\35\3\35\3\35\3\36\6"+
		"\36\u009f\n\36\r\36\16\36\u00a0\3\36\3\36\2\2\37\3\3\5\4\7\5\t\6\13\7"+
		"\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25"+
		")\26+\27-\30/\31\61\32\63\33\65\34\67\29\35;\36\3\2\6\4\2C\\c|\n\2$$)"+
		")^^ddhhppttvv\4\2$$^^\4\2\13\f\"\"\2\u00a8\2\3\3\2\2\2\2\5\3\2\2\2\2\7"+
		"\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2"+
		"\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2"+
		"\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2"+
		"\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2"+
		"\2\65\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\3=\3\2\2\2\5@\3\2\2\2\7B\3\2\2\2\t"+
		"E\3\2\2\2\13G\3\2\2\2\rI\3\2\2\2\17L\3\2\2\2\21O\3\2\2\2\23Q\3\2\2\2\25"+
		"S\3\2\2\2\27U\3\2\2\2\31W\3\2\2\2\33Y\3\2\2\2\35]\3\2\2\2\37a\3\2\2\2"+
		"!e\3\2\2\2#h\3\2\2\2%m\3\2\2\2\'s\3\2\2\2)v\3\2\2\2+y\3\2\2\2-|\3\2\2"+
		"\2/\177\3\2\2\2\61\u0081\3\2\2\2\63\u0084\3\2\2\2\65\u0088\3\2\2\2\67"+
		"\u0090\3\2\2\29\u0093\3\2\2\2;\u009e\3\2\2\2=>\7>\2\2>?\7/\2\2?\4\3\2"+
		"\2\2@A\7?\2\2A\6\3\2\2\2BC\7\61\2\2CD\7?\2\2D\b\3\2\2\2EF\7@\2\2F\n\3"+
		"\2\2\2GH\7>\2\2H\f\3\2\2\2IJ\7@\2\2JK\7?\2\2K\16\3\2\2\2LM\7>\2\2MN\7"+
		"?\2\2N\20\3\2\2\2OP\7-\2\2P\22\3\2\2\2QR\7/\2\2R\24\3\2\2\2ST\7,\2\2T"+
		"\26\3\2\2\2UV\7\61\2\2V\30\3\2\2\2WX\7\'\2\2X\32\3\2\2\2YZ\7>\2\2Z[\7"+
		"A\2\2[\\\7@\2\2\\\34\3\2\2\2]^\7>\2\2^_\7#\2\2_`\7@\2\2`\36\3\2\2\2ab"+
		"\7>\2\2bc\7<\2\2cd\7@\2\2d \3\2\2\2ef\7k\2\2fg\7h\2\2g\"\3\2\2\2hi\7g"+
		"\2\2ij\7n\2\2jk\7u\2\2kl\7g\2\2l$\3\2\2\2mn\7y\2\2no\7j\2\2op\7k\2\2p"+
		"q\7n\2\2qr\7g\2\2r&\3\2\2\2st\7>\2\2tu\7>\2\2u(\3\2\2\2vw\7:\2\2wx\7>"+
		"\2\2x*\3\2\2\2yz\7~\2\2z{\7<\2\2{,\3\2\2\2|}\7<\2\2}~\7~\2\2~.\3\2\2\2"+
		"\177\u0080\4\62;\2\u0080\60\3\2\2\2\u0081\u0082\t\2\2\2\u0082\62\3\2\2"+
		"\2\u0083\u0085\5/\30\2\u0084\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0084"+
		"\3\2\2\2\u0086\u0087\3\2\2\2\u0087\64\3\2\2\2\u0088\u008d\5\61\31\2\u0089"+
		"\u008c\5\61\31\2\u008a\u008c\5/\30\2\u008b\u0089\3\2\2\2\u008b\u008a\3"+
		"\2\2\2\u008c\u008f\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e"+
		"\66\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u0091\7^\2\2\u0091\u0092\t\3\2\2"+
		"\u00928\3\2\2\2\u0093\u0098\7$\2\2\u0094\u0097\5\67\34\2\u0095\u0097\n"+
		"\4\2\2\u0096\u0094\3\2\2\2\u0096\u0095\3\2\2\2\u0097\u009a\3\2\2\2\u0098"+
		"\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009b\3\2\2\2\u009a\u0098\3\2"+
		"\2\2\u009b\u009c\7$\2\2\u009c:\3\2\2\2\u009d\u009f\t\5\2\2\u009e\u009d"+
		"\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1"+
		"\u00a2\3\2\2\2\u00a2\u00a3\b\36\2\2\u00a3<\3\2\2\2\t\2\u0086\u008b\u008d"+
		"\u0096\u0098\u00a0\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}