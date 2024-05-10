/* tslint:disable */
/* eslint-disable */
/**
 * FastAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { mapValues } from '../runtime';
import type { DownloadData } from './DownloadData';
import {
    DownloadDataFromJSON,
    DownloadDataFromJSONTyped,
    DownloadDataToJSON,
} from './DownloadData';

/**
 * 
 * @export
 * @interface DownloadItem
 */
export interface DownloadItem {
    /**
     * 
     * @type {string}
     * @memberof DownloadItem
     */
    message?: string;
    /**
     * 
     * @type {boolean}
     * @memberof DownloadItem
     */
    success?: boolean;
    /**
     * 
     * @type {string}
     * @memberof DownloadItem
     */
    title?: string;
    /**
     * 
     * @type {DownloadData}
     * @memberof DownloadItem
     */
    data?: DownloadData;
}

/**
 * Check if a given object implements the DownloadItem interface.
 */
export function instanceOfDownloadItem(value: object): boolean {
    return true;
}

export function DownloadItemFromJSON(json: any): DownloadItem {
    return DownloadItemFromJSONTyped(json, false);
}

export function DownloadItemFromJSONTyped(json: any, ignoreDiscriminator: boolean): DownloadItem {
    if (json == null) {
        return json;
    }
    return {
        
        'message': json['message'] == null ? undefined : json['message'],
        'success': json['success'] == null ? undefined : json['success'],
        'title': json['title'] == null ? undefined : json['title'],
        'data': json['data'] == null ? undefined : DownloadDataFromJSON(json['data']),
    };
}

export function DownloadItemToJSON(value?: DownloadItem | null): any {
    if (value == null) {
        return value;
    }
    return {
        
        'message': value['message'],
        'success': value['success'],
        'title': value['title'],
        'data': DownloadDataToJSON(value['data']),
    };
}

