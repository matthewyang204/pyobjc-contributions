# This file is generated by objective.metadata
#
# Last update: Fri May 10 14:09:29 2024
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$NLContextualEmbeddingKeyLanguages$NLContextualEmbeddingKeyRevision$NLContextualEmbeddingKeyScripts$NLLanguageAmharic$NLLanguageArabic$NLLanguageArmenian$NLLanguageBengali$NLLanguageBulgarian$NLLanguageBurmese$NLLanguageCatalan$NLLanguageCherokee$NLLanguageCroatian$NLLanguageCzech$NLLanguageDanish$NLLanguageDutch$NLLanguageEnglish$NLLanguageFinnish$NLLanguageFrench$NLLanguageGeorgian$NLLanguageGerman$NLLanguageGreek$NLLanguageGujarati$NLLanguageHebrew$NLLanguageHindi$NLLanguageHungarian$NLLanguageIcelandic$NLLanguageIndonesian$NLLanguageItalian$NLLanguageJapanese$NLLanguageKannada$NLLanguageKazakh$NLLanguageKhmer$NLLanguageKorean$NLLanguageLao$NLLanguageMalay$NLLanguageMalayalam$NLLanguageMarathi$NLLanguageMongolian$NLLanguageNorwegian$NLLanguageOriya$NLLanguagePersian$NLLanguagePolish$NLLanguagePortuguese$NLLanguagePunjabi$NLLanguageRomanian$NLLanguageRussian$NLLanguageSimplifiedChinese$NLLanguageSinhalese$NLLanguageSlovak$NLLanguageSpanish$NLLanguageSwedish$NLLanguageTamil$NLLanguageTelugu$NLLanguageThai$NLLanguageTibetan$NLLanguageTraditionalChinese$NLLanguageTurkish$NLLanguageUkrainian$NLLanguageUndetermined$NLLanguageUrdu$NLLanguageVietnamese$NLScriptArabic$NLScriptArmenian$NLScriptBengali$NLScriptCanadianAboriginalSyllabics$NLScriptCherokee$NLScriptCyrillic$NLScriptDevanagari$NLScriptEthiopic$NLScriptGeorgian$NLScriptGreek$NLScriptGujarati$NLScriptGurmukhi$NLScriptHebrew$NLScriptJapanese$NLScriptKannada$NLScriptKhmer$NLScriptKorean$NLScriptLao$NLScriptLatin$NLScriptMalayalam$NLScriptMongolian$NLScriptMyanmar$NLScriptOriya$NLScriptSimplifiedChinese$NLScriptSinhala$NLScriptTamil$NLScriptTelugu$NLScriptThai$NLScriptTibetan$NLScriptTraditionalChinese$NLScriptUndetermined$NLTagAdjective$NLTagAdverb$NLTagClassifier$NLTagCloseParenthesis$NLTagCloseQuote$NLTagConjunction$NLTagDash$NLTagDeterminer$NLTagIdiom$NLTagInterjection$NLTagNoun$NLTagNumber$NLTagOpenParenthesis$NLTagOpenQuote$NLTagOrganizationName$NLTagOther$NLTagOtherPunctuation$NLTagOtherWhitespace$NLTagOtherWord$NLTagParagraphBreak$NLTagParticle$NLTagPersonalName$NLTagPlaceName$NLTagPreposition$NLTagPronoun$NLTagPunctuation$NLTagSchemeLanguage$NLTagSchemeLemma$NLTagSchemeLexicalClass$NLTagSchemeNameType$NLTagSchemeNameTypeOrLexicalClass$NLTagSchemeScript$NLTagSchemeSentimentScore$NLTagSchemeTokenType$NLTagSentenceTerminator$NLTagVerb$NLTagWhitespace$NLTagWord$NLTagWordJoiner$"""
enums = """$NLContextualEmbeddingAssetsResultAvailable@0$NLContextualEmbeddingAssetsResultError@2$NLContextualEmbeddingAssetsResultNotAvailable@1$NLDistanceTypeCosine@0$NLModelTypeClassifier@0$NLModelTypeSequence@1$NLTaggerAssetsResultAvailable@0$NLTaggerAssetsResultError@2$NLTaggerAssetsResultNotAvailable@1$NLTaggerJoinContractions@32$NLTaggerJoinNames@16$NLTaggerOmitOther@8$NLTaggerOmitPunctuation@2$NLTaggerOmitWhitespace@4$NLTaggerOmitWords@1$NLTokenUnitDocument@3$NLTokenUnitParagraph@2$NLTokenUnitSentence@1$NLTokenUnitWord@0$NLTokenizerAttributeEmoji@4$NLTokenizerAttributeNumeric@1$NLTokenizerAttributeSymbolic@2$"""
misc.update(
    {
        "NLContextualEmbeddingAssetsResult": NewType(
            "NLContextualEmbeddingAssetsResult", int
        ),
        "NLModelType": NewType("NLModelType", int),
        "NLTokenUnit": NewType("NLTokenUnit", int),
        "NLDistanceType": NewType("NLDistanceType", int),
        "NLTaggerAssetsResult": NewType("NLTaggerAssetsResult", int),
        "NLTaggerOptions": NewType("NLTaggerOptions", int),
        "NLTokenizerAttributes": NewType("NLTokenizerAttributes", int),
    }
)
misc.update(
    {
        "NLTagScheme": NewType("NLTagScheme", str),
        "NLLanguage": NewType("NLLanguage", str),
        "NLContextualEmbeddingKey": NewType("NLContextualEmbeddingKey", str),
        "NLTag": NewType("NLTag", str),
        "NLScript": NewType("NLScript", str),
    }
)
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NLContextualEmbedding",
        b"embeddingResultForString:language:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(b"NLContextualEmbedding", b"hasAvailableAssets", {"retval": {"type": b"Z"}})
    r(
        b"NLContextualEmbedding",
        b"loadWithError:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"NLContextualEmbedding",
        b"requestEmbeddingAssetsWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"q"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"NLContextualEmbeddingResult",
        b"enumerateTokenVectorsInRange:usingBlock:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"{_NSRange=QQ}"},
                            3: {"type": b"o^Z"},
                        },
                    }
                }
            }
        },
    )
    r(b"NLEmbedding", b"containsString:", {"retval": {"type": b"Z"}})
    r(
        b"NLEmbedding",
        b"embeddingWithContentsOfURL:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NLEmbedding",
        b"enumerateNeighborsForString:maximumCount:distanceType:usingBlock:",
        {
            "arguments": {
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"d"},
                            3: {"type": b"o^Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"NLEmbedding",
        b"enumerateNeighborsForString:maximumCount:maximumDistance:distanceType:usingBlock:",
        {
            "arguments": {
                6: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"d"},
                            3: {"type": b"o^Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"NLEmbedding",
        b"enumerateNeighborsForVector:maximumCount:distanceType:usingBlock:",
        {
            "arguments": {
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"d"},
                            3: {"type": b"o^Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"NLEmbedding",
        b"enumerateNeighborsForVector:maximumCount:maximumDistance:distanceType:usingBlock:",
        {
            "arguments": {
                6: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"d"},
                            3: {"type": b"o^Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"NLEmbedding",
        b"getVector:forString:",
        {
            "retval": {"type": b"Z"},
            "arguments": {
                2: {"type_modifier": b"o", "c_array_of_variable_length": True}
            },
        },
    )
    r(
        b"NLEmbedding",
        b"writeEmbeddingForDictionary:language:revision:toURL:error:",
        {"retval": {"type": b"Z"}, "arguments": {6: {"type_modifier": b"o"}}},
    )
    r(
        b"NLGazetteer",
        b"gazetteerWithContentsOfURL:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NLGazetteer",
        b"initWithContentsOfURL:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NLGazetteer",
        b"initWithData:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NLGazetteer",
        b"initWithDictionary:language:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"NLGazetteer",
        b"writeGazetteerForDictionary:language:toURL:error:",
        {"retval": {"type": b"Z"}, "arguments": {5: {"type_modifier": b"o"}}},
    )
    r(
        b"NLModel",
        b"modelWithContentsOfURL:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NLModel",
        b"modelWithMLModel:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"NLTagger",
        b"enumerateTagsInRange:unit:scheme:options:usingBlock:",
        {
            "arguments": {
                6: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"{_NSRange=QQ}"},
                            3: {"type": b"o^Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"NLTagger",
        b"requestAssetsForLanguage:tagScheme:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"q"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"NLTagger",
        b"tagHypothesesAtIndex:unit:scheme:maximumCount:tokenRange:",
        {"arguments": {6: {"type_modifier": b"o"}}},
    )
    r(
        b"NLTokenizer",
        b"enumerateTokensInRange:usingBlock:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"{_NSRange=QQ}"},
                            2: {"type": b"Q"},
                            3: {"type": b"o^Z"},
                        },
                    }
                }
            }
        },
    )
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector("NLGazetteer", b"initWithContentsOfURL:error:")
objc.registerNewKeywordsFromSelector("NLGazetteer", b"initWithData:error:")
objc.registerNewKeywordsFromSelector(
    "NLGazetteer", b"initWithDictionary:language:error:"
)
objc.registerNewKeywordsFromSelector("NLTagger", b"initWithTagSchemes:")
objc.registerNewKeywordsFromSelector("NLTokenizer", b"initWithUnit:")
expressions = {}

# END OF FILE
