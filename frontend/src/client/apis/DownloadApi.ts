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


import * as runtime from '../runtime';
import type {
  DownloadItem,
  DownloadResponse,
  HTTPValidationError,
} from '../models/index';
import {
    DownloadItemFromJSON,
    DownloadItemToJSON,
    DownloadResponseFromJSON,
    DownloadResponseToJSON,
    HTTPValidationErrorFromJSON,
    HTTPValidationErrorToJSON,
} from '../models/index';

export interface GetDownloadV1DownloadDownloadIdGetRequest {
    downloadId: string;
    xToken: string;
}

export interface GetDownloadsV1DownloadAllGetRequest {
    xToken: string;
}

export interface PauseDownloadV1DownloadPauseDownloadIdGetRequest {
    downloadId: string;
    xToken: string;
}

export interface RemoveDownloadV1DownloadRemoveDownloadIdGetRequest {
    downloadId: string;
    xToken: string;
}

export interface ResumeDownloadV1DownloadResumeDownloadIdGetRequest {
    downloadId: string;
    xToken: string;
}

/**
 * 
 */
export class DownloadApi extends runtime.BaseAPI {

    /**
     * Get Download
     */
    async getDownloadV1DownloadDownloadIdGetRaw(requestParameters: GetDownloadV1DownloadDownloadIdGetRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<DownloadItem>> {
        if (requestParameters['downloadId'] == null) {
            throw new runtime.RequiredError(
                'downloadId',
                'Required parameter "downloadId" was null or undefined when calling getDownloadV1DownloadDownloadIdGet().'
            );
        }

        if (requestParameters['xToken'] == null) {
            throw new runtime.RequiredError(
                'xToken',
                'Required parameter "xToken" was null or undefined when calling getDownloadV1DownloadDownloadIdGet().'
            );
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (requestParameters['xToken'] != null) {
            headerParameters['x-token'] = String(requestParameters['xToken']);
        }

        const response = await this.request({
            path: `/v1/download/{download_id}`.replace(`{${"download_id"}}`, encodeURIComponent(String(requestParameters['downloadId']))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => DownloadItemFromJSON(jsonValue));
    }

    /**
     * Get Download
     */
    async getDownloadV1DownloadDownloadIdGet(requestParameters: GetDownloadV1DownloadDownloadIdGetRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<DownloadItem> {
        const response = await this.getDownloadV1DownloadDownloadIdGetRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Get Downloads
     */
    async getDownloadsV1DownloadAllGetRaw(requestParameters: GetDownloadsV1DownloadAllGetRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<DownloadResponse>> {
        if (requestParameters['xToken'] == null) {
            throw new runtime.RequiredError(
                'xToken',
                'Required parameter "xToken" was null or undefined when calling getDownloadsV1DownloadAllGet().'
            );
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (requestParameters['xToken'] != null) {
            headerParameters['x-token'] = String(requestParameters['xToken']);
        }

        const response = await this.request({
            path: `/v1/download/all`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => DownloadResponseFromJSON(jsonValue));
    }

    /**
     * Get Downloads
     */
    async getDownloadsV1DownloadAllGet(requestParameters: GetDownloadsV1DownloadAllGetRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<DownloadResponse> {
        const response = await this.getDownloadsV1DownloadAllGetRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Pause Download
     */
    async pauseDownloadV1DownloadPauseDownloadIdGetRaw(requestParameters: PauseDownloadV1DownloadPauseDownloadIdGetRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<DownloadItem>> {
        if (requestParameters['downloadId'] == null) {
            throw new runtime.RequiredError(
                'downloadId',
                'Required parameter "downloadId" was null or undefined when calling pauseDownloadV1DownloadPauseDownloadIdGet().'
            );
        }

        if (requestParameters['xToken'] == null) {
            throw new runtime.RequiredError(
                'xToken',
                'Required parameter "xToken" was null or undefined when calling pauseDownloadV1DownloadPauseDownloadIdGet().'
            );
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (requestParameters['xToken'] != null) {
            headerParameters['x-token'] = String(requestParameters['xToken']);
        }

        const response = await this.request({
            path: `/v1/download/pause/{download_id}`.replace(`{${"download_id"}}`, encodeURIComponent(String(requestParameters['downloadId']))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => DownloadItemFromJSON(jsonValue));
    }

    /**
     * Pause Download
     */
    async pauseDownloadV1DownloadPauseDownloadIdGet(requestParameters: PauseDownloadV1DownloadPauseDownloadIdGetRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<DownloadItem> {
        const response = await this.pauseDownloadV1DownloadPauseDownloadIdGetRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Remove Download
     */
    async removeDownloadV1DownloadRemoveDownloadIdGetRaw(requestParameters: RemoveDownloadV1DownloadRemoveDownloadIdGetRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<DownloadItem>> {
        if (requestParameters['downloadId'] == null) {
            throw new runtime.RequiredError(
                'downloadId',
                'Required parameter "downloadId" was null or undefined when calling removeDownloadV1DownloadRemoveDownloadIdGet().'
            );
        }

        if (requestParameters['xToken'] == null) {
            throw new runtime.RequiredError(
                'xToken',
                'Required parameter "xToken" was null or undefined when calling removeDownloadV1DownloadRemoveDownloadIdGet().'
            );
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (requestParameters['xToken'] != null) {
            headerParameters['x-token'] = String(requestParameters['xToken']);
        }

        const response = await this.request({
            path: `/v1/download/remove/{download_id}`.replace(`{${"download_id"}}`, encodeURIComponent(String(requestParameters['downloadId']))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => DownloadItemFromJSON(jsonValue));
    }

    /**
     * Remove Download
     */
    async removeDownloadV1DownloadRemoveDownloadIdGet(requestParameters: RemoveDownloadV1DownloadRemoveDownloadIdGetRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<DownloadItem> {
        const response = await this.removeDownloadV1DownloadRemoveDownloadIdGetRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Resume Download
     */
    async resumeDownloadV1DownloadResumeDownloadIdGetRaw(requestParameters: ResumeDownloadV1DownloadResumeDownloadIdGetRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<DownloadItem>> {
        if (requestParameters['downloadId'] == null) {
            throw new runtime.RequiredError(
                'downloadId',
                'Required parameter "downloadId" was null or undefined when calling resumeDownloadV1DownloadResumeDownloadIdGet().'
            );
        }

        if (requestParameters['xToken'] == null) {
            throw new runtime.RequiredError(
                'xToken',
                'Required parameter "xToken" was null or undefined when calling resumeDownloadV1DownloadResumeDownloadIdGet().'
            );
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (requestParameters['xToken'] != null) {
            headerParameters['x-token'] = String(requestParameters['xToken']);
        }

        const response = await this.request({
            path: `/v1/download/resume/{download_id}`.replace(`{${"download_id"}}`, encodeURIComponent(String(requestParameters['downloadId']))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => DownloadItemFromJSON(jsonValue));
    }

    /**
     * Resume Download
     */
    async resumeDownloadV1DownloadResumeDownloadIdGet(requestParameters: ResumeDownloadV1DownloadResumeDownloadIdGetRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<DownloadItem> {
        const response = await this.resumeDownloadV1DownloadResumeDownloadIdGetRaw(requestParameters, initOverrides);
        return await response.value();
    }

}
