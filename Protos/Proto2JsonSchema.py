import sys
import os.path
import argparse
import importlib
import json

from google.protobuf import descriptor
from google.protobuf import descriptor_pool


g_field_type_to_name= {
    descriptor.FieldDescriptor.TYPE_DOUBLE   : 'TYPE_DOUBLE',
    descriptor.FieldDescriptor.TYPE_FLOAT    : 'TYPE_FLOAT',
    descriptor.FieldDescriptor.TYPE_INT64    : 'TYPE_INT64',
    descriptor.FieldDescriptor.TYPE_UINT64   : 'TYPE_UINT64',
    descriptor.FieldDescriptor.TYPE_INT32    : 'TYPE_INT32',
    descriptor.FieldDescriptor.TYPE_FIXED64  : 'TYPE_FIXED64',
    descriptor.FieldDescriptor.TYPE_FIXED32  : 'TYPE_FIXED32',
    descriptor.FieldDescriptor.TYPE_BOOL     : 'TYPE_BOOL',
    descriptor.FieldDescriptor.TYPE_STRING   : 'TYPE_STRING',
    descriptor.FieldDescriptor.TYPE_BYTES    : 'TYPE_BYTES',
    descriptor.FieldDescriptor.TYPE_UINT32   : 'TYPE_UINT32',
    descriptor.FieldDescriptor.TYPE_SFIXED32 : 'TYPE_SFIXED32',
    descriptor.FieldDescriptor.TYPE_SFIXED64 : 'TYPE_SFIXED64',
    descriptor.FieldDescriptor.TYPE_SINT32   : 'TYPE_SINT32',
    descriptor.FieldDescriptor.TYPE_SINT64   : 'TYPE_SINT64',
}


def get_ref_inner( ref_name ) :
    return '#/definitions/{0}'.format( ref_name )

def get_ref_outter( definitions_file_name, ref_name ) :
    return '{definition}#/definitions/{ref}'.format( definition= definitions_file_name, ref= ref_name )

def get_type_ref( field_type ) :
    return get_ref_inner( g_field_type_to_name[field_type] )


def get_base_definitions() :
    return {
        g_field_type_to_name[descriptor.FieldDescriptor.TYPE_DOUBLE] : {
            'type' : 'number',
        },
        g_field_type_to_name[descriptor.FieldDescriptor.TYPE_FLOAT] : {
            '$ref' : get_type_ref( descriptor.FieldDescriptor.TYPE_DOUBLE ),
        },
        g_field_type_to_name[descriptor.FieldDescriptor.TYPE_INT64] : {
            'type' : 'integer',
            'minimum' : -2**63,
            'maximum' : 2**63 - 1,
        },
        g_field_type_to_name[descriptor.FieldDescriptor.TYPE_UINT64] : {
            'type' : 'integer',
            'minimum' : 0,
            'maximum' : 2**64 - 1,
        },
        g_field_type_to_name[descriptor.FieldDescriptor.TYPE_INT32] : {
            'type' : 'integer',
            'minimum' : -2**31,
            'maximum' : 2**31 - 1,
        },
        g_field_type_to_name[descriptor.FieldDescriptor.TYPE_FIXED64] : {
            '$ref' : get_type_ref( descriptor.FieldDescriptor.TYPE_UINT64 ),
        },
        g_field_type_to_name[descriptor.FieldDescriptor.TYPE_FIXED32] : {
            '$ref' : get_type_ref( descriptor.FieldDescriptor.TYPE_UINT32 ),
        },
        g_field_type_to_name[descriptor.FieldDescriptor.TYPE_BOOL] : {
            'type' : 'boolean',
        },
        g_field_type_to_name[descriptor.FieldDescriptor.TYPE_STRING] : {
            'type' : 'string',
        },
        g_field_type_to_name[descriptor.FieldDescriptor.TYPE_BYTES] : {
            '$ref' : get_type_ref( descriptor.FieldDescriptor.TYPE_STRING ),
        },
        g_field_type_to_name[descriptor.FieldDescriptor.TYPE_UINT32] : {
            'type' : 'integer',
            'minimum' : 0,
            'maximum' : 2**32 - 1,
        },
        g_field_type_to_name[descriptor.FieldDescriptor.TYPE_SFIXED32] : {
            '$ref' : get_type_ref( descriptor.FieldDescriptor.TYPE_INT32 ),
        },
        g_field_type_to_name[descriptor.FieldDescriptor.TYPE_SFIXED64] : {
            '$ref' : get_type_ref( descriptor.FieldDescriptor.TYPE_INT64 ),
        },
        g_field_type_to_name[descriptor.FieldDescriptor.TYPE_SINT32] : {
            '$ref' : get_type_ref( descriptor.FieldDescriptor.TYPE_INT32 ),
        },
        g_field_type_to_name[descriptor.FieldDescriptor.TYPE_SINT64] : {
            '$ref' : get_type_ref( descriptor.FieldDescriptor.TYPE_INT64 ),
        },
        'google.protobuf.DoubleValue' : {
            '$ref' : get_type_ref( descriptor.FieldDescriptor.TYPE_DOUBLE ),
        },
        'google.protobuf.FloatValue' : {
            '$ref' : get_type_ref( descriptor.FieldDescriptor.TYPE_FLOAT ),
        },
        'google.protobuf.Int64Value' : {
            '$ref' : get_type_ref( descriptor.FieldDescriptor.TYPE_INT64 ),
        },
        'google.protobuf.UInt64Value' : {
            '$ref' : get_type_ref( descriptor.FieldDescriptor.TYPE_UINT64 ),
        },
        'google.protobuf.Int32Value' : {
            '$ref' : get_type_ref( descriptor.FieldDescriptor.TYPE_INT32 ),
        },
        'google.protobuf.UInt32Value' : {
            '$ref' : get_type_ref( descriptor.FieldDescriptor.TYPE_UINT32 ),
        },
        'google.protobuf.BoolValue' : {
            '$ref' : get_type_ref( descriptor.FieldDescriptor.TYPE_BOOL ),
        },
        'google.protobuf.StringValue' : {
            '$ref' : get_type_ref( descriptor.FieldDescriptor.TYPE_STRING ),
        },
        'google.protobuf.BytesValue' : {
            '$ref' : get_type_ref( descriptor.FieldDescriptor.TYPE_BYTES ),
        },
    }


def prepare_field_definition( definitions, field_desc ) : # return ref_name
    if field_desc.type == descriptor.FieldDescriptor.TYPE_MESSAGE :
        return prepare_msg_definition( definitions, field_desc.message_type )
    elif field_desc.type == descriptor.FieldDescriptor.TYPE_ENUM :
        return prepare_enum_definition( definitions, field_desc.enum_type )
    else :
        return g_field_type_to_name[field_desc.type]


def prepare_enum_definition( definitions, enum_desc ) : # return enum_ref_name
    enum_ref_name= enum_desc.full_name
    if enum_ref_name not in definitions :
        rule= {
            'type' : 'string',
            'enum' : [],
        }
        definitions[enum_ref_name]= rule
        enums= rule['enum']
        for enum_value_desc in enum_desc.values :
            enums.append( enum_value_desc.name )
    return enum_ref_name


def is_map_field( field_desc ) :
    return ( field_desc.type == descriptor.FieldDescriptor.TYPE_MESSAGE and
             field_desc.message_type.has_options and
             field_desc.message_type.GetOptions().map_entry )


def prepare_msg_definition( definitions, msg_desc ) : # return msg_ref_name
    msg_ref_name= msg_desc.full_name
    if msg_ref_name not in definitions :
        rule= {
            'type' : 'object',
        }
        definitions[msg_ref_name]= rule
        properties= {}
        required= []
        for field_desc in msg_desc.fields :
            assert field_desc.json_name not in properties
            field_rule= None
            if is_map_field( field_desc ) :
                value_field_desc= field_desc.message_type.fields_by_name['value']
                value_field_ref_name= prepare_field_definition( definitions, value_field_desc )
                value_field_ref= get_ref_inner( value_field_ref_name )
                field_rule= {
                    'type' : 'object',
                    'additionalProperties' : {
                        '$ref' : value_field_ref,
                    },
                }
            else :
                field_ref_name= prepare_field_definition( definitions, field_desc )
                field_ref= get_ref_inner( field_ref_name )
                if field_desc.label == descriptor.FieldDescriptor.LABEL_REPEATED :
                    field_rule= {
                        'type' : 'array',
                        'items' : {
                            '$ref' : field_ref,
                        },
                    }
                elif field_desc.type == descriptor.FieldDescriptor.TYPE_MESSAGE :
                    field_rule= {
                        'oneOf' : [
                            {
                                'type' : 'null',
                            },
                            {
                                '$ref' : field_ref,
                            },
                        ],
                    }
                else :
                    field_rule= {
                        '$ref' : field_ref,
                    }
            assert field_rule is not None
            properties[field_desc.json_name]= field_rule
            if field_desc.label == descriptor.FieldDescriptor.LABEL_REQUIRED :
                required.append( field_desc.json_name )
        if properties :
            rule['properties']= properties
        if required :
            rule['required']= required
    return msg_ref_name


def output_json( out_path, sort_keys, file_name, schema ) :
    path= os.path.join( out_path, file_name )
    path= os.path.abspath( path )
    with open( path, 'w' ) as f :
        json.dump( schema, f, indent= 4, separators= ( ',', ' : ' ), sort_keys= sort_keys )


def output_msg_schema( out_path, sort_keys, mono, meta_schema, definitions_file_name, msg_name, definitions, msg_ref_name ) :
    if mono :
        schema= {
            '$schema' : meta_schema,
            'definitions' : definitions,
            '$ref' : get_ref_inner( msg_ref_name ),
        }
    else :
        schema= {
            '$schema' : meta_schema,
            '$ref' : get_ref_outter( definitions_file_name, msg_ref_name ),
        }
    output_json( out_path, sort_keys, msg_name + '.json', schema )


def output_definitions( out_path, sort_keys, meta_schema, definitions_file_name, definitions ) :
    schema= {
        '$schema' : meta_schema,
        'definitions' : definitions,
    }
    output_json( out_path, sort_keys, definitions_file_name, schema )


def main( args ) :
    for in_path in args.in_paths :
        sys.path.append( os.path.abspath( in_path ) )
    for pb_module in args.pb_modules :
        importlib.import_module( pb_module )
    definitions= None
    for msg_name in args.messages :
        if definitions is None or args.mono :
            definitions= get_base_definitions()
        msg_desc= descriptor_pool.Default().FindMessageTypeByName( msg_name )
        msg_ref_name= prepare_msg_definition( definitions, msg_desc )
        output_msg_schema( args.out_path, args.sort_keys, args.mono, args.meta_schema, args.definitions_file_name, msg_name, definitions, msg_ref_name )
    if not args.mono :
        output_definitions( args.out_path, args.sort_keys, args.meta_schema, args.definitions_file_name, definitions )


if __name__ == '__main__' :
    parser= argparse.ArgumentParser( description= 'generate json schema from protobuf' )
    parser.add_argument( '-o', '--out', metavar= 'path', dest= 'out_path', required= True, help= 'schema output path' )
    parser.add_argument( '-d', '--definitions', metavar= 'definitions_file_name', dest= 'definitions_file_name', default= 'definitions.json', help= 'file name for definitions json, without directory name. default to "definitions.json"' )
    parser.add_argument( '-s', '--sort', action='store_true', default= False, dest= 'sort_keys', help= 'sort json properties by key' )
    parser.add_argument( '--mono', action='store_true', default= False, dest= 'mono', help= 'include definitions in message schema file' )
    parser.add_argument( '--meta_schema', metavar= 'uri', dest= 'meta_schema', default= 'http://json-schema.org/schema#', help= 'schema of schema' )
    parser.add_argument( '-i', '--in', action= 'append', metavar= 'path', dest= 'in_paths', help= 'path to import module from' )
    parser.add_argument( '-m', '--module', action= 'append', metavar= 'pb_module', dest= 'pb_modules', required= True, help= 'protobuf module to import' )
    parser.add_argument( 'messages', nargs= '+', metavar= 'message', help= 'proto messages to generate schema for' )
    args= parser.parse_args()
    main( args )

