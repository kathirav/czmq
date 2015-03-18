/*  =========================================================================
    zdir_patch - work with directory patches

    Copyright (c) the Contributors as noted in the AUTHORS file.
    This file is part of CZMQ, the high-level C binding for 0MQ:
    http://czmq.zeromq.org.

    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at http://mozilla.org/MPL/2.0/.
    =========================================================================
*/

#ifndef __ZDIR_PATCH_H_INCLUDED__
#define __ZDIR_PATCH_H_INCLUDED__

#ifdef __cplusplus
extern "C" {
#endif

// un-namespaced enumeration values
#define patch_create ZDIR_PATCH_CREATE
#define patch_delete ZDIR_PATCH_DELETE

//  @warning THE FOLLOWING @INTERFACE BLOCK IS AUTO-GENERATED BY ZPROJECT!
//  @warning Please edit the model at "api/zdir_patch.xml" to make changes.
//  @interface
typedef enum {
    ZDIR_PATCH_CREATE = 1,
    ZDIR_PATCH_DELETE = 2
} zdir_patch_op_t;

//  Create new patch
CZMQ_EXPORT zdir_patch_t *
    zdir_patch_new (const char *path, zfile_t *file, zdir_patch_op_t op, const char *alias);

//  Destroy a patch
CZMQ_EXPORT void
    zdir_patch_destroy (zdir_patch_t **self_p);

//  Create copy of a patch. If the patch is null, or memory was exhausted,          
//  returns null.                                                                   
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zdir_patch_t *
    zdir_patch_dup (zdir_patch_t *self);

//  Return patch file directory path
CZMQ_EXPORT const char *
    zdir_patch_path (zdir_patch_t *self);

//  Return patch file item
CZMQ_EXPORT zfile_t *
    zdir_patch_file (zdir_patch_t *self);

//  Return operation
CZMQ_EXPORT zdir_patch_op_t
    zdir_patch_op (zdir_patch_t *self);

//  Return patch virtual file path
CZMQ_EXPORT const char *
    zdir_patch_vpath (zdir_patch_t *self);

//  Calculate hash digest for file (create only)
CZMQ_EXPORT void
    zdir_patch_digest_set (zdir_patch_t *self);

//  Return hash digest for patch file
CZMQ_EXPORT const char *
    zdir_patch_digest (zdir_patch_t *self);

//  Self test of this class.
CZMQ_EXPORT void
    zdir_patch_test (bool verbose);
//  @end

#ifdef __cplusplus
}
#endif

#endif
