# This file is generated by objective.metadata
#
# Last update: Fri May 10 12:17:40 2024
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
constants = """$MLFeatureValueImageOptionCropAndScale$MLFeatureValueImageOptionCropRect$MLModelAuthorKey$MLModelCollectionDidChangeNotification$MLModelCreatorDefinedKey$MLModelDescriptionKey$MLModelErrorDomain$MLModelLicenseKey$MLModelVersionStringKey$"""
enums = """$MLComputeUnitsAll@2$MLComputeUnitsCPUAndGPU@1$MLComputeUnitsCPUAndNeuralEngine@3$MLComputeUnitsCPUOnly@0$MLFeatureTypeDictionary@6$MLFeatureTypeDouble@2$MLFeatureTypeImage@4$MLFeatureTypeInt64@1$MLFeatureTypeInvalid@0$MLFeatureTypeMultiArray@5$MLFeatureTypeSequence@7$MLFeatureTypeString@3$MLImageSizeConstraintTypeEnumerated@2$MLImageSizeConstraintTypeRange@3$MLImageSizeConstraintTypeUnspecified@0$MLModelErrorCustomLayer@4$MLModelErrorCustomModel@5$MLModelErrorFeatureType@1$MLModelErrorGeneric@0$MLModelErrorIO@3$MLModelErrorModelCollection@10$MLModelErrorModelDecryption@9$MLModelErrorModelDecryptionKeyFetch@8$MLModelErrorParameters@7$MLModelErrorPredictionCancelled@11$MLModelErrorUpdate@6$MLMultiArrayDataTypeDouble@65600$MLMultiArrayDataTypeFloat@65568$MLMultiArrayDataTypeFloat16@65552$MLMultiArrayDataTypeFloat32@65568$MLMultiArrayDataTypeFloat64@65600$MLMultiArrayDataTypeInt32@131104$MLMultiArrayShapeConstraintTypeEnumerated@2$MLMultiArrayShapeConstraintTypeRange@3$MLMultiArrayShapeConstraintTypeUnspecified@1$MLReshapeFrequencyHintFrequent@0$MLReshapeFrequencyHintInfrequent@1$MLTaskStateCancelling@3$MLTaskStateCompleted@4$MLTaskStateFailed@5$MLTaskStateRunning@2$MLTaskStateSuspended@1$MLUpdateProgressEventEpochEnd@2$MLUpdateProgressEventMiniBatchEnd@4$MLUpdateProgressEventTrainingBegin@1$"""
misc.update(
    {
        "MLMultiArrayDataType": NewType("MLMultiArrayDataType", int),
        "MLMultiArrayShapeConstraintType": NewType(
            "MLMultiArrayShapeConstraintType", int
        ),
        "MLImageSizeConstraintType": NewType("MLImageSizeConstraintType", int),
        "MLTaskState": NewType("MLTaskState", int),
        "MLUpdateProgressEvent": NewType("MLUpdateProgressEvent", int),
        "MLFeatureType": NewType("MLFeatureType", int),
        "MLModelError": NewType("MLModelError", int),
        "MLComputeUnits": NewType("MLComputeUnits", int),
        "MLReshapeFrequencyHint": NewType("MLReshapeFrequencyHint", int),
    }
)
misc.update(
    {
        "MLFeatureValueImageOption": NewType("MLFeatureValueImageOption", str),
        "MLModelMetadataKey": NewType("MLModelMetadataKey", str),
    }
)
misc.update({})
functions = {"MLAllComputeDevices": (b"@",)}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"MLArrayBatchProvider",
        b"initWithDictionary:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"MLComputePlan",
        b"loadContentsOfURL:configuration:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MLComputePlan",
        b"loadModelAsset:configuration:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MLDictionaryFeatureProvider",
        b"initWithDictionary:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(b"MLFeatureDescription", b"isAllowedValue:", {"retval": {"type": "Z"}})
    r(b"MLFeatureDescription", b"isOptional", {"retval": {"type": "Z"}})
    r(b"MLFeatureDescription", b"setOptional:", {"arguments": {2: {"type": "Z"}}})
    r(
        b"MLFeatureValue",
        b"featureValueWithCGImage:constraint:options:error:",
        {"arguments": {5: {"type_modifier": b"o"}}},
    )
    r(
        b"MLFeatureValue",
        b"featureValueWithCGImage:orientation:constraint:options:error:",
        {"arguments": {6: {"type_modifier": b"o"}}},
    )
    r(
        b"MLFeatureValue",
        b"featureValueWithCGImage:orientation:pixelsWide:pixelsHigh:pixelFormatType:options:error:",
        {"arguments": {8: {"type_modifier": b"o"}}},
    )
    r(
        b"MLFeatureValue",
        b"featureValueWithCGImage:pixelsWide:pixelsHigh:pixelFormatType:options:error:",
        {"arguments": {7: {"type_modifier": b"o"}}},
    )
    r(
        b"MLFeatureValue",
        b"featureValueWithDictionary:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"MLFeatureValue",
        b"featureValueWithImageAtURL:constraint:options:error:",
        {"arguments": {5: {"type_modifier": b"o"}}},
    )
    r(
        b"MLFeatureValue",
        b"featureValueWithImageAtURL:orientation:constraint:options:error:",
        {"arguments": {6: {"type_modifier": b"o"}}},
    )
    r(
        b"MLFeatureValue",
        b"featureValueWithImageAtURL:orientation:pixelsWide:pixelsHigh:pixelFormatType:options:error:",
        {"arguments": {8: {"type_modifier": b"o"}}},
    )
    r(
        b"MLFeatureValue",
        b"featureValueWithImageAtURL:pixelsWide:pixelsHigh:pixelFormatType:options:error:",
        {"arguments": {7: {"type_modifier": b"o"}}},
    )
    r(b"MLFeatureValue", b"isEqualToFeatureValue:", {"retval": {"type": "Z"}})
    r(b"MLFeatureValue", b"isUndefined", {"retval": {"type": "Z"}})
    r(
        b"MLModel",
        b"compileModelAtURL:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MLModel",
        b"compileModelAtURL:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"MLModel",
        b"loadContentsOfURL:configuration:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MLModel",
        b"loadModelAsset:configuration:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MLModel",
        b"modelWithContentsOfURL:configuration:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"MLModel",
        b"modelWithContentsOfURL:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"MLModel",
        b"parameterValueForKey:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"MLModel",
        b"predictionFromFeatures:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MLModel",
        b"predictionFromFeatures:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"MLModel",
        b"predictionFromFeatures:options:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MLModel",
        b"predictionFromFeatures:options:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"MLModel",
        b"predictionsFromBatch:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"MLModel",
        b"predictionsFromBatch:options:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"MLModelAsset",
        b"modelAssetWithSpecificationData:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"MLModelCollection",
        b"beginAccessingModelCollectionWithIdentifier:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MLModelCollection",
        b"endAccessingModelCollectionWithIdentifier:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MLModelCollectionEntry",
        b"isEqualToModelCollectionEntry:",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"MLModelConfiguration",
        b"allowLowPrecisionAccumulationOnGPU",
        {"retval": {"type": "Z"}},
    )
    r(
        b"MLModelConfiguration",
        b"setAllowLowPrecisionAccumulationOnGPU:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(b"MLModelDescription", b"isUpdatable", {"retval": {"type": b"Z"}})
    r(
        b"MLModelStructure",
        b"loadContentsOfURL:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MLModelStructure",
        b"loadModelAsset:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(b"MLMultiArray", b"dataPointer", {"retval": {"c_array_of_variable_length": True}})
    r(
        b"MLMultiArray",
        b"getBytesWithHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"n^v", "c_array_length_in_arg": 2},
                            2: {"type": b"q"},
                        },
                    }
                },
                7: {"type_modifier": b"o"},
            }
        },
    )
    r(
        b"MLMultiArray",
        b"getMutableBytesWithHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"N^v", "c_array_length_in_arg": 2},
                            2: {"type": b"q"},
                            3: {"type": b"@"},
                        },
                    }
                },
                7: {"type_modifier": b"o"},
            }
        },
    )
    r(
        b"MLMultiArray",
        b"initWithDataPointer:shape:dataType:strides:deallocator:error:",
        {
            "arguments": {
                2: {"type_modifier": b"n", "c_array_of_variable_length": True},
                6: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"^v"}},
                    }
                },
                7: {"type_modifier": b"o"},
            }
        },
    )
    r(
        b"MLMultiArray",
        b"initWithShape:dataType:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(b"MLPredictionOptions", b"setUsesCPUOnly:", {"arguments": {2: {"type": "Z"}}})
    r(b"MLPredictionOptions", b"usesCPUOnly", {"retval": {"type": "Z"}})
    r(
        b"MLUpdateProgressHandlers",
        b"initForEvents:progressHandler:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                },
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                },
            }
        },
    )
    r(
        b"MLUpdateTask",
        b"updateTaskForModelAtURL:trainingData:completionHandler:error:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                },
                5: {"type_modifier": b"o"},
            }
        },
    )
    r(
        b"MLUpdateTask",
        b"updateTaskForModelAtURL:trainingData:configuration:completionHandler:error:",
        {
            "arguments": {
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                },
                6: {"type_modifier": b"o"},
            }
        },
    )
    r(
        b"MLUpdateTask",
        b"updateTaskForModelAtURL:trainingData:configuration:progressHandlers:error:",
        {
            "arguments": {
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                },
                6: {"type_modifier": b"o"},
            }
        },
    )
    r(
        b"MLUpdateTask",
        b"updateTaskForModelAtURL:trainingData:progressHandlers:error:",
        {"arguments": {5: {"type_modifier": b"o"}}},
    )
    r(b"NSObject", b"count", {"required": True, "retval": {"type": "q"}})
    r(
        b"NSObject",
        b"encodeToCommandBuffer:inputs:outputs:error:",
        {
            "required": False,
            "retval": {"type": "Z"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"@"},
                5: {"type": "^@", "type_modifier": b"o"},
            },
        },
    )
    r(
        b"NSObject",
        b"evaluateOnCPUWithInputs:outputs:error:",
        {
            "required": True,
            "retval": {"type": "Z"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": "^@", "type_modifier": b"o"},
            },
        },
    )
    r(b"NSObject", b"featureNames", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"featureProviderAtIndex:",
        {"required": False, "retval": {"type": b"@"}, "arguments": {2: {"type": b"q"}}},
    )
    r(
        b"NSObject",
        b"featureProviderCount",
        {"required": False, "retval": {"type": b"q"}},
    )
    r(
        b"NSObject",
        b"featureValueForName:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"featuresAtIndex:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": "q"}}},
    )
    r(
        b"NSObject",
        b"initWithModelDescription:parameterDictionary:error:",
        {
            "required": True,
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": "^@", "type_modifier": b"o"},
            },
        },
    )
    r(
        b"NSObject",
        b"initWithParameterDictionary:error:",
        {
            "required": True,
            "retval": {"type": b"@"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "^@", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"outputShapesForInputShapes:error:",
        {
            "required": True,
            "retval": {"type": b"@"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "^@", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"predictionFromFeatures:options:error:",
        {
            "required": True,
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": "^@", "type_modifier": b"o"},
            },
        },
    )
    r(
        b"NSObject",
        b"predictionsFromBatch:options:error:",
        {
            "required": False,
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": "^@", "type_modifier": b"o"},
            },
        },
    )
    r(
        b"NSObject",
        b"setWeightData:error:",
        {
            "required": True,
            "retval": {"type": "Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "^@", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"writeToURL:error:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "o^@", "type_modifier": b"o"}},
        },
    )
    r(b"null", b"allowLowPrecisionAccumulationOnGPU", {"retval": {"type": b"Z"}})
    r(
        b"null",
        b"featureValueWithCGImage:constraint:options:error:",
        {"arguments": {5: {"type_modifier": b"o"}}},
    )
    r(
        b"null",
        b"featureValueWithCGImage:orientation:constraint:options:error:",
        {"arguments": {6: {"type_modifier": b"o"}}},
    )
    r(
        b"null",
        b"featureValueWithCGImage:orientation:pixelsWide:pixelsHigh:pixelFormatType:options:error:",
        {"arguments": {8: {"type_modifier": b"o"}}},
    )
    r(
        b"null",
        b"featureValueWithCGImage:pixelsWide:pixelsHigh:pixelFormatType:options:error:",
        {"arguments": {7: {"type_modifier": b"o"}}},
    )
    r(
        b"null",
        b"featureValueWithImageAtURL:constraint:options:error:",
        {"arguments": {5: {"type_modifier": b"o"}}},
    )
    r(
        b"null",
        b"featureValueWithImageAtURL:orientation:constraint:options:error:",
        {"arguments": {6: {"type_modifier": b"o"}}},
    )
    r(
        b"null",
        b"featureValueWithImageAtURL:orientation:pixelsWide:pixelsHigh:pixelFormatType:options:error:",
        {"arguments": {8: {"type_modifier": b"o"}}},
    )
    r(
        b"null",
        b"featureValueWithImageAtURL:pixelsWide:pixelsHigh:pixelFormatType:options:error:",
        {"arguments": {7: {"type_modifier": b"o"}}},
    )
    r(b"null", b"isUpdatable", {"retval": {"type": b"Z"}})
    r(
        b"null",
        b"setAllowLowPrecisionAccumulationOnGPU:",
        {"arguments": {2: {"type": b"Z"}}},
    )
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector(
    "MLArrayBatchProvider", b"initWithDictionary:error:"
)
objc.registerNewKeywordsFromSelector(
    "MLArrayBatchProvider", b"initWithFeatureProviderArray:"
)
objc.registerNewKeywordsFromSelector(
    "MLDictionaryFeatureProvider", b"initWithDictionary:error:"
)
objc.registerNewKeywordsFromSelector(
    "MLMultiArray", b"initWithDataPointer:shape:dataType:strides:deallocator:error:"
)
objc.registerNewKeywordsFromSelector("MLMultiArray", b"initWithPixelBuffer:shape:")
objc.registerNewKeywordsFromSelector("MLMultiArray", b"initWithShape:dataType:error:")
objc.registerNewKeywordsFromSelector(
    "MLUpdateProgressHandlers", b"initForEvents:progressHandler:completionHandler:"
)
expressions = {}

# END OF FILE
