# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: scip/scip.proto
# Protobuf Python Version: 5.29.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    3,
    '',
    'scip/scip.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fscip/scip.proto\x12\x04scip\"\x7f\n\x05Index\x12 \n\x08metadata\x18\x01 \x01(\x0b\x32\x0e.scip.Metadata\x12!\n\tdocuments\x18\x02 \x03(\x0b\x32\x0e.scip.Document\x12\x31\n\x10\x65xternal_symbols\x18\x03 \x03(\x0b\x32\x17.scip.SymbolInformation\"\x9f\x01\n\x08Metadata\x12&\n\x07version\x18\x01 \x01(\x0e\x32\x15.scip.ProtocolVersion\x12!\n\ttool_info\x18\x02 \x01(\x0b\x32\x0e.scip.ToolInfo\x12\x14\n\x0cproject_root\x18\x03 \x01(\t\x12\x32\n\x16text_document_encoding\x18\x04 \x01(\x0e\x32\x12.scip.TextEncoding\"<\n\x08ToolInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x11\n\targuments\x18\x03 \x03(\t\"\xc5\x01\n\x08\x44ocument\x12\x10\n\x08language\x18\x04 \x01(\t\x12\x15\n\rrelative_path\x18\x01 \x01(\t\x12%\n\x0boccurrences\x18\x02 \x03(\x0b\x32\x10.scip.Occurrence\x12(\n\x07symbols\x18\x03 \x03(\x0b\x32\x17.scip.SymbolInformation\x12\x0c\n\x04text\x18\x05 \x01(\t\x12\x31\n\x11position_encoding\x18\x06 \x01(\x0e\x32\x16.scip.PositionEncoding\"_\n\x06Symbol\x12\x0e\n\x06scheme\x18\x01 \x01(\t\x12\x1e\n\x07package\x18\x02 \x01(\x0b\x32\r.scip.Package\x12%\n\x0b\x64\x65scriptors\x18\x03 \x03(\x0b\x32\x10.scip.Descriptor\"9\n\x07Package\x12\x0f\n\x07manager\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\"\x82\x02\n\nDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rdisambiguator\x18\x02 \x01(\t\x12\'\n\x06suffix\x18\x03 \x01(\x0e\x32\x17.scip.Descriptor.Suffix\"\xa5\x01\n\x06Suffix\x12\x15\n\x11UnspecifiedSuffix\x10\x00\x12\r\n\tNamespace\x10\x01\x12\x0f\n\x07Package\x10\x01\x1a\x02\x08\x01\x12\x08\n\x04Type\x10\x02\x12\x08\n\x04Term\x10\x03\x12\n\n\x06Method\x10\x04\x12\x11\n\rTypeParameter\x10\x05\x12\r\n\tParameter\x10\x06\x12\x08\n\x04Meta\x10\x07\x12\t\n\x05Local\x10\x08\x12\t\n\x05Macro\x10\t\x1a\x02\x10\x01\"\xf0\x0b\n\x11SymbolInformation\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x15\n\rdocumentation\x18\x03 \x03(\t\x12)\n\rrelationships\x18\x04 \x03(\x0b\x32\x12.scip.Relationship\x12*\n\x04kind\x18\x05 \x01(\x0e\x32\x1c.scip.SymbolInformation.Kind\x12\x14\n\x0c\x64isplay_name\x18\x06 \x01(\t\x12/\n\x17signature_documentation\x18\x07 \x01(\x0b\x32\x0e.scip.Document\x12\x18\n\x10\x65nclosing_symbol\x18\x08 \x01(\t\"\xfb\t\n\x04Kind\x12\x13\n\x0fUnspecifiedKind\x10\x00\x12\x12\n\x0e\x41\x62stractMethod\x10\x42\x12\x0c\n\x08\x41\x63\x63\x65ssor\x10H\x12\t\n\x05\x41rray\x10\x01\x12\r\n\tAssertion\x10\x02\x12\x12\n\x0e\x41ssociatedType\x10\x03\x12\r\n\tAttribute\x10\x04\x12\t\n\x05\x41xiom\x10\x05\x12\x0b\n\x07\x42oolean\x10\x06\x12\t\n\x05\x43lass\x10\x07\x12\x0b\n\x07\x43oncept\x10V\x12\x0c\n\x08\x43onstant\x10\x08\x12\x0f\n\x0b\x43onstructor\x10\t\x12\x0c\n\x08\x43ontract\x10>\x12\x0e\n\nDataFamily\x10\n\x12\x0c\n\x08\x44\x65legate\x10I\x12\x08\n\x04\x45num\x10\x0b\x12\x0e\n\nEnumMember\x10\x0c\x12\t\n\x05\x45rror\x10?\x12\t\n\x05\x45vent\x10\r\x12\r\n\tExtension\x10T\x12\x08\n\x04\x46\x61\x63t\x10\x0e\x12\t\n\x05\x46ield\x10\x0f\x12\x08\n\x04\x46ile\x10\x10\x12\x0c\n\x08\x46unction\x10\x11\x12\n\n\x06Getter\x10\x12\x12\x0b\n\x07Grammar\x10\x13\x12\x0c\n\x08Instance\x10\x14\x12\r\n\tInterface\x10\x15\x12\x07\n\x03Key\x10\x16\x12\x08\n\x04Lang\x10\x17\x12\t\n\x05Lemma\x10\x18\x12\x0b\n\x07Library\x10@\x12\t\n\x05Macro\x10\x19\x12\n\n\x06Method\x10\x1a\x12\x0f\n\x0bMethodAlias\x10J\x12\x12\n\x0eMethodReceiver\x10\x1b\x12\x17\n\x13MethodSpecification\x10\x43\x12\x0b\n\x07Message\x10\x1c\x12\t\n\x05Mixin\x10U\x12\x0c\n\x08Modifier\x10\x41\x12\n\n\x06Module\x10\x1d\x12\r\n\tNamespace\x10\x1e\x12\x08\n\x04Null\x10\x1f\x12\n\n\x06Number\x10 \x12\n\n\x06Object\x10!\x12\x0c\n\x08Operator\x10\"\x12\x0b\n\x07Package\x10#\x12\x11\n\rPackageObject\x10$\x12\r\n\tParameter\x10%\x12\x12\n\x0eParameterLabel\x10&\x12\x0b\n\x07Pattern\x10\'\x12\r\n\tPredicate\x10(\x12\x0c\n\x08Property\x10)\x12\x0c\n\x08Protocol\x10*\x12\x12\n\x0eProtocolMethod\x10\x44\x12\x15\n\x11PureVirtualMethod\x10\x45\x12\x0f\n\x0bQuasiquoter\x10+\x12\x11\n\rSelfParameter\x10,\x12\n\n\x06Setter\x10-\x12\r\n\tSignature\x10.\x12\x12\n\x0eSingletonClass\x10K\x12\x13\n\x0fSingletonMethod\x10L\x12\x14\n\x10StaticDataMember\x10M\x12\x0f\n\x0bStaticEvent\x10N\x12\x0f\n\x0bStaticField\x10O\x12\x10\n\x0cStaticMethod\x10P\x12\x12\n\x0eStaticProperty\x10Q\x12\x12\n\x0eStaticVariable\x10R\x12\n\n\x06String\x10\x30\x12\n\n\x06Struct\x10\x31\x12\r\n\tSubscript\x10/\x12\n\n\x06Tactic\x10\x32\x12\x0b\n\x07Theorem\x10\x33\x12\x11\n\rThisParameter\x10\x34\x12\t\n\x05Trait\x10\x35\x12\x0f\n\x0bTraitMethod\x10\x46\x12\x08\n\x04Type\x10\x36\x12\r\n\tTypeAlias\x10\x37\x12\r\n\tTypeClass\x10\x38\x12\x13\n\x0fTypeClassMethod\x10G\x12\x0e\n\nTypeFamily\x10\x39\x12\x11\n\rTypeParameter\x10:\x12\t\n\x05Union\x10;\x12\t\n\x05Value\x10<\x12\x0c\n\x08Variable\x10=\"\x82\x01\n\x0cRelationship\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x14\n\x0cis_reference\x18\x02 \x01(\x08\x12\x19\n\x11is_implementation\x18\x03 \x01(\x08\x12\x1a\n\x12is_type_definition\x18\x04 \x01(\x08\x12\x15\n\ris_definition\x18\x05 \x01(\x08\"\xc8\x01\n\nOccurrence\x12\r\n\x05range\x18\x01 \x03(\x05\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x14\n\x0csymbol_roles\x18\x03 \x01(\x05\x12\x1e\n\x16override_documentation\x18\x04 \x03(\t\x12%\n\x0bsyntax_kind\x18\x05 \x01(\x0e\x32\x10.scip.SyntaxKind\x12%\n\x0b\x64iagnostics\x18\x06 \x03(\x0b\x32\x10.scip.Diagnostic\x12\x17\n\x0f\x65nclosing_range\x18\x07 \x03(\x05\"\x80\x01\n\nDiagnostic\x12 \n\x08severity\x18\x01 \x01(\x0e\x32\x0e.scip.Severity\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x04 \x01(\t\x12!\n\x04tags\x18\x05 \x03(\x0e\x32\x13.scip.DiagnosticTag*1\n\x0fProtocolVersion\x12\x1e\n\x1aUnspecifiedProtocolVersion\x10\x00*@\n\x0cTextEncoding\x12\x1b\n\x17UnspecifiedTextEncoding\x10\x00\x12\x08\n\x04UTF8\x10\x01\x12\t\n\x05UTF16\x10\x02*\xa4\x01\n\x10PositionEncoding\x12\x1f\n\x1bUnspecifiedPositionEncoding\x10\x00\x12#\n\x1fUTF8CodeUnitOffsetFromLineStart\x10\x01\x12$\n UTF16CodeUnitOffsetFromLineStart\x10\x02\x12$\n UTF32CodeUnitOffsetFromLineStart\x10\x03*\x94\x01\n\nSymbolRole\x12\x19\n\x15UnspecifiedSymbolRole\x10\x00\x12\x0e\n\nDefinition\x10\x01\x12\n\n\x06Import\x10\x02\x12\x0f\n\x0bWriteAccess\x10\x04\x12\x0e\n\nReadAccess\x10\x08\x12\r\n\tGenerated\x10\x10\x12\x08\n\x04Test\x10 \x12\x15\n\x11\x46orwardDefinition\x10@*\xea\x06\n\nSyntaxKind\x12\x19\n\x15UnspecifiedSyntaxKind\x10\x00\x12\x0b\n\x07\x43omment\x10\x01\x12\x18\n\x14PunctuationDelimiter\x10\x02\x12\x16\n\x12PunctuationBracket\x10\x03\x12\x0b\n\x07Keyword\x10\x04\x12\x19\n\x11IdentifierKeyword\x10\x04\x1a\x02\x08\x01\x12\x16\n\x12IdentifierOperator\x10\x05\x12\x0e\n\nIdentifier\x10\x06\x12\x15\n\x11IdentifierBuiltin\x10\x07\x12\x12\n\x0eIdentifierNull\x10\x08\x12\x16\n\x12IdentifierConstant\x10\t\x12\x1b\n\x17IdentifierMutableGlobal\x10\n\x12\x17\n\x13IdentifierParameter\x10\x0b\x12\x13\n\x0fIdentifierLocal\x10\x0c\x12\x16\n\x12IdentifierShadowed\x10\r\x12\x17\n\x13IdentifierNamespace\x10\x0e\x12\x18\n\x10IdentifierModule\x10\x0e\x1a\x02\x08\x01\x12\x16\n\x12IdentifierFunction\x10\x0f\x12 \n\x1cIdentifierFunctionDefinition\x10\x10\x12\x13\n\x0fIdentifierMacro\x10\x11\x12\x1d\n\x19IdentifierMacroDefinition\x10\x12\x12\x12\n\x0eIdentifierType\x10\x13\x12\x19\n\x15IdentifierBuiltinType\x10\x14\x12\x17\n\x13IdentifierAttribute\x10\x15\x12\x0f\n\x0bRegexEscape\x10\x16\x12\x11\n\rRegexRepeated\x10\x17\x12\x11\n\rRegexWildcard\x10\x18\x12\x12\n\x0eRegexDelimiter\x10\x19\x12\r\n\tRegexJoin\x10\x1a\x12\x11\n\rStringLiteral\x10\x1b\x12\x17\n\x13StringLiteralEscape\x10\x1c\x12\x18\n\x14StringLiteralSpecial\x10\x1d\x12\x14\n\x10StringLiteralKey\x10\x1e\x12\x14\n\x10\x43haracterLiteral\x10\x1f\x12\x12\n\x0eNumericLiteral\x10 \x12\x12\n\x0e\x42ooleanLiteral\x10!\x12\x07\n\x03Tag\x10\"\x12\x10\n\x0cTagAttribute\x10#\x12\x10\n\x0cTagDelimiter\x10$\x1a\x02\x10\x01*V\n\x08Severity\x12\x17\n\x13UnspecifiedSeverity\x10\x00\x12\t\n\x05\x45rror\x10\x01\x12\x0b\n\x07Warning\x10\x02\x12\x0f\n\x0bInformation\x10\x03\x12\x08\n\x04Hint\x10\x04*N\n\rDiagnosticTag\x12\x1c\n\x18UnspecifiedDiagnosticTag\x10\x00\x12\x0f\n\x0bUnnecessary\x10\x01\x12\x0e\n\nDeprecated\x10\x02*\x9b\n\n\x08Language\x12\x17\n\x13UnspecifiedLanguage\x10\x00\x12\x08\n\x04\x41\x42\x41P\x10<\x12\x08\n\x04\x41pex\x10`\x12\x07\n\x03\x41PL\x10\x31\x12\x07\n\x03\x41\x64\x61\x10\'\x12\x08\n\x04\x41gda\x10-\x12\x0c\n\x08\x41sciiDoc\x10V\x12\x0c\n\x08\x41ssembly\x10:\x12\x07\n\x03\x41wk\x10\x42\x12\x07\n\x03\x42\x61t\x10\x44\x12\n\n\x06\x42ibTeX\x10Q\x12\x05\n\x01\x43\x10\"\x12\t\n\x05\x43OBOL\x10;\x12\x07\n\x03\x43PP\x10#\x12\x07\n\x03\x43SS\x10\x1a\x12\n\n\x06\x43Sharp\x10\x01\x12\x0b\n\x07\x43lojure\x10\x08\x12\x10\n\x0c\x43offeescript\x10\x15\x12\x0e\n\nCommonLisp\x10\t\x12\x07\n\x03\x43oq\x10/\x12\x08\n\x04\x43UDA\x10\x61\x12\x08\n\x04\x44\x61rt\x10\x03\x12\n\n\x06\x44\x65lphi\x10\x39\x12\x08\n\x04\x44iff\x10X\x12\x0e\n\nDockerfile\x10P\x12\n\n\x06\x44yalog\x10\x32\x12\n\n\x06\x45lixir\x10\x11\x12\n\n\x06\x45rlang\x10\x12\x12\n\n\x06\x46Sharp\x10*\x12\x08\n\x04\x46ish\x10\x41\x12\x08\n\x04\x46low\x10\x18\x12\x0b\n\x07\x46ortran\x10\x38\x12\x0e\n\nGit_Commit\x10[\x12\x0e\n\nGit_Config\x10Y\x12\x0e\n\nGit_Rebase\x10\\\x12\x06\n\x02Go\x10!\x12\x0b\n\x07GraphQL\x10\x62\x12\n\n\x06Groovy\x10\x07\x12\x08\n\x04HTML\x10\x1e\x12\x08\n\x04Hack\x10\x14\x12\x0e\n\nHandlebars\x10Z\x12\x0b\n\x07Haskell\x10,\x12\t\n\x05Idris\x10.\x12\x07\n\x03Ini\x10H\x12\x05\n\x01J\x10\x33\x12\x08\n\x04JSON\x10K\x12\x08\n\x04Java\x10\x06\x12\x0e\n\nJavaScript\x10\x16\x12\x13\n\x0fJavaScriptReact\x10]\x12\x0b\n\x07Jsonnet\x10L\x12\t\n\x05Julia\x10\x37\x12\x0c\n\x08Justfile\x10m\x12\n\n\x06Kotlin\x10\x04\x12\t\n\x05LaTeX\x10S\x12\x08\n\x04Lean\x10\x30\x12\x08\n\x04Less\x10\x1b\x12\x07\n\x03Lua\x10\x0c\x12\x08\n\x04Luau\x10l\x12\x0c\n\x08Makefile\x10O\x12\x0c\n\x08Markdown\x10T\x12\n\n\x06Matlab\x10\x34\x12\n\n\x06Nickel\x10n\x12\x07\n\x03Nix\x10M\x12\t\n\x05OCaml\x10)\x12\x0f\n\x0bObjective_C\x10$\x12\x11\n\rObjective_CPP\x10%\x12\n\n\x06Pascal\x10\x63\x12\x07\n\x03PHP\x10\x13\x12\t\n\x05PLSQL\x10\x46\x12\x08\n\x04Perl\x10\r\x12\x0e\n\nPowerShell\x10\x43\x12\n\n\x06Prolog\x10G\x12\x0c\n\x08Protobuf\x10\x64\x12\n\n\x06Python\x10\x0f\x12\x05\n\x01R\x10\x36\x12\n\n\x06Racket\x10\x0b\x12\x08\n\x04Raku\x10\x0e\x12\t\n\x05Razor\x10>\x12\t\n\x05Repro\x10\x66\x12\x08\n\x04ReST\x10U\x12\x08\n\x04Ruby\x10\x10\x12\x08\n\x04Rust\x10(\x12\x07\n\x03SAS\x10=\x12\x08\n\x04SCSS\x10\x1d\x12\x07\n\x03SML\x10+\x12\x07\n\x03SQL\x10\x45\x12\x08\n\x04Sass\x10\x1c\x12\t\n\x05Scala\x10\x05\x12\n\n\x06Scheme\x10\n\x12\x0f\n\x0bShellScript\x10@\x12\x0b\n\x07Skylark\x10N\x12\t\n\x05Slang\x10k\x12\x0c\n\x08Solidity\x10_\x12\n\n\x06Svelte\x10j\x12\t\n\x05Swift\x10\x02\x12\x07\n\x03Tcl\x10\x65\x12\x08\n\x04TOML\x10I\x12\x07\n\x03TeX\x10R\x12\n\n\x06Thrift\x10g\x12\x0e\n\nTypeScript\x10\x17\x12\x13\n\x0fTypeScriptReact\x10^\x12\x0b\n\x07Verilog\x10h\x12\x08\n\x04VHDL\x10i\x12\x0f\n\x0bVisualBasic\x10?\x12\x07\n\x03Vue\x10\x19\x12\x0b\n\x07Wolfram\x10\x35\x12\x07\n\x03XML\x10\x1f\x12\x07\n\x03XSL\x10 \x12\x08\n\x04YAML\x10J\x12\x07\n\x03Zig\x10&B/Z-github.com/sourcegraph/scip/bindings/go/scip/b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'scip.scip_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z-github.com/sourcegraph/scip/bindings/go/scip/'
  _globals['_SYNTAXKIND']._loaded_options = None
  _globals['_SYNTAXKIND']._serialized_options = b'\020\001'
  _globals['_SYNTAXKIND'].values_by_name["IdentifierKeyword"]._loaded_options = None
  _globals['_SYNTAXKIND'].values_by_name["IdentifierKeyword"]._serialized_options = b'\010\001'
  _globals['_SYNTAXKIND'].values_by_name["IdentifierModule"]._loaded_options = None
  _globals['_SYNTAXKIND'].values_by_name["IdentifierModule"]._serialized_options = b'\010\001'
  _globals['_DESCRIPTOR_SUFFIX']._loaded_options = None
  _globals['_DESCRIPTOR_SUFFIX']._serialized_options = b'\020\001'
  _globals['_DESCRIPTOR_SUFFIX'].values_by_name["Package"]._loaded_options = None
  _globals['_DESCRIPTOR_SUFFIX'].values_by_name["Package"]._serialized_options = b'\010\001'
  _globals['_PROTOCOLVERSION']._serialized_start=2985
  _globals['_PROTOCOLVERSION']._serialized_end=3034
  _globals['_TEXTENCODING']._serialized_start=3036
  _globals['_TEXTENCODING']._serialized_end=3100
  _globals['_POSITIONENCODING']._serialized_start=3103
  _globals['_POSITIONENCODING']._serialized_end=3267
  _globals['_SYMBOLROLE']._serialized_start=3270
  _globals['_SYMBOLROLE']._serialized_end=3418
  _globals['_SYNTAXKIND']._serialized_start=3421
  _globals['_SYNTAXKIND']._serialized_end=4295
  _globals['_SEVERITY']._serialized_start=4297
  _globals['_SEVERITY']._serialized_end=4383
  _globals['_DIAGNOSTICTAG']._serialized_start=4385
  _globals['_DIAGNOSTICTAG']._serialized_end=4463
  _globals['_LANGUAGE']._serialized_start=4466
  _globals['_LANGUAGE']._serialized_end=5773
  _globals['_INDEX']._serialized_start=25
  _globals['_INDEX']._serialized_end=152
  _globals['_METADATA']._serialized_start=155
  _globals['_METADATA']._serialized_end=314
  _globals['_TOOLINFO']._serialized_start=316
  _globals['_TOOLINFO']._serialized_end=376
  _globals['_DOCUMENT']._serialized_start=379
  _globals['_DOCUMENT']._serialized_end=576
  _globals['_SYMBOL']._serialized_start=578
  _globals['_SYMBOL']._serialized_end=673
  _globals['_PACKAGE']._serialized_start=675
  _globals['_PACKAGE']._serialized_end=732
  _globals['_DESCRIPTOR']._serialized_start=735
  _globals['_DESCRIPTOR']._serialized_end=993
  _globals['_DESCRIPTOR_SUFFIX']._serialized_start=828
  _globals['_DESCRIPTOR_SUFFIX']._serialized_end=993
  _globals['_SYMBOLINFORMATION']._serialized_start=996
  _globals['_SYMBOLINFORMATION']._serialized_end=2516
  _globals['_SYMBOLINFORMATION_KIND']._serialized_start=1241
  _globals['_SYMBOLINFORMATION_KIND']._serialized_end=2516
  _globals['_RELATIONSHIP']._serialized_start=2519
  _globals['_RELATIONSHIP']._serialized_end=2649
  _globals['_OCCURRENCE']._serialized_start=2652
  _globals['_OCCURRENCE']._serialized_end=2852
  _globals['_DIAGNOSTIC']._serialized_start=2855
  _globals['_DIAGNOSTIC']._serialized_end=2983
# @@protoc_insertion_point(module_scope)
